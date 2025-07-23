from tuya_connector import TuyaOpenAPI
import json
from tabulate import tabulate
import csv


# === Configuration ===
ACCESS_ID = 'your_access_id_here'  # Replace with your actual Access ID
ACCESS_KEY = 'your_access_key_here'  # Replace with your actual Access Key

# Select the region based on your project
# Available regions: 'us', 'eu', 'cn', 'in'
REGION = 'eu'  # Change this to your desired region
ENDPOINTS = {
    'us': "https://openapi.tuyaus.com",
    'eu': "https://openapi.tuyaeu.com",
    'cn': "https://openapi.tuyacn.com",
    'in': "https://openapi.tuyain.com",
}
API_ENDPOINT = ENDPOINTS[REGION]

# ── Api conexion ───────────────────────────────────────
api = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
api.connect()

# ── Obtain devices ───────────────────────────────
fouindAll = False
last_id = None
devices = []
while not fouindAll:

    if last_id:
        resp = api.get("/v2.0/cloud/thing/device", params={ "page_size": 20, "last_id": last_id })
    else:
        resp = api.get("/v2.0/cloud/thing/device", params={ "page_size": 20 })
    if resp.get("success") is False:
        print("Error al obtener dispositivos:", resp.get("msg"))
        exit(1)
        
    result = resp.get("result", {})
    if not resp or result is None or     len(result) == 0:
        foundAll = True
        break
    
    
    devices.extend(result)
    last_id = result[-1].get("id") if result else None
    
    # Guardar los dispositivos en un archivo CSV
    with open("devices.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre", "ID"])
        for dev in result:
            writer.writerow([dev.get("name"), dev.get("id")])
    for dev in result:
        print(f"Dispositivo encontrado: {dev.get('name')} ({dev.get('id')})")
            
if not devices:
    print("No se encontraron dispositivos o la API no devolvio resultados.")
    exit(1)

# ── FOR EACH DEVICE, GET DETAILS AND LOCAL_KEY ──────

table = []
for dev in devices:
    dev_id = dev.get("id")
    name = dev.get("name")
    given_name = dev.get("customName", name)
    info = api.get(f"/v1.0/devices/{dev_id}")
    result = info.get("result", {})
    local_key = result.get("local_key")
    table.append([given_name,name,  dev_id, local_key])

print(tabulate(table, headers=["Given Name", "Name", "ID", "Local Key"], tablefmt="grid"))