# Tuya Device Info Extractor

This Python script connects to the Tuya Cloud API, retrieves a list of your devices, and exports their details (including the local key) to the console and a CSV file.

## Features

- Connects to Tuya Cloud API using your credentials.
- Fetches all devices from your Tuya account.
- Saves device names and IDs to `devices.csv`.
- Displays a table with device names, IDs, and local keys.

## Requirements

- Python 3.x
- [tuya-connector](https://pypi.org/project/tuya-connector/)
- [tabulate](https://pypi.org/project/tabulate/)

Install dependencies with:

```sh
pip install tuya-connector tabulate
```

## How to Obtain Tuya API Credentials

1. **Create a Tuya IoT Platform Account**
   - Go to [Tuya IoT Platform](https://iot.tuya.com/) and sign up or log in.

2. **Create a Cloud Project**
   - Click on "Cloud" in the top menu, then "Development".
   - Click "Create Cloud Project".
   - Fill in the project name, select your region, and choose "Smart Home" as the industry.
   - After creation, go to the project details.

3. **Link Devices to Your Project**
   - In your project, go to the "Link Tuya App Account" section.
   - Click "Add App Account" and scan the QR code with the Tuya Smart app (or Smart Life app) on your phone.
   - Log in with the same account you use for your devices.

4. **Get Your API Credentials**
   - In your project overview, you will see:
     - **Access ID** (also called Client ID)
     - **Access Secret** (also called Client Secret)
   - Copy these values and paste them into the script as `ACCESS_ID` and `ACCESS_KEY`.

5. **Select the Correct Region**
   - Use the region that matches your Tuya account and project (e.g., `eu`, `us`, `cn`, `in`).

## Usage

1. Edit the script to set your `ACCESS_ID`, `ACCESS_KEY`, and `REGION` at the top.
2. Run the script:

```sh
python tuya.py
```

3. The script will:
   - Print found devices to the console.
   - Save device names and IDs to `devices.csv`.
   - Display a table with device details and local keys.

## Notes

- The script uses the Tuya OpenAPI. Make sure your credentials and region are correct.
- The local key is required for some local integrations (e.g., Home Assistant).

##
