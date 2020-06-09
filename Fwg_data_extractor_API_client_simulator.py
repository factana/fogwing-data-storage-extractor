import requests
import json


def extract_data_API():

    # Reading configuration file.
    with open('configuration.json', 'r') as file:
        config = json.load(file)

    # Fogwing Platform credentials reading from configuration file.
    username = config['Fwg_Platform_cred']['username']
    password = config['Fwg_Platform_cred']['password']

    # Fogwing IoTHub credentials reading from configuration file.
    client_id = config['Fwg_IoTHub_cred']['client_id']
    dev_eui = config['Fwg_IoTHub_cred']['dev_eui']
    mac_id = config['Fwg_IoTHub_cred']['mac_id']

    # Duration period of datalog reading from configuration file.
    start_date = config['fetch_data']['start_date']
    end_date = config['fetch_data']['end_date']

    credentials = {"user_name": username, "password": password}
    api_key_url = 'https://non-prod.fogwing.net/api/dlogapi/Data Stream API Methods/getApiKey'
    resp = requests.post(api_key_url, json=credentials, verify=False)
    resp_dict = json.loads(resp.text)
    api_key = resp_dict['token']

    header = {"API-KEY": api_key}
    payload_url = 'https://non-prod.fogwing.net/api/dlogapi/Data Stream API Methods/getdatastream/{}/{}/{}/{}/{}' \
        .format(client_id, mac_id, dev_eui, start_date, end_date)
    payload_resp = requests.get(payload_url, headers=header, verify=False)
    data = json.loads(payload_resp.text)
    formatted_payload_resp = json.dumps(data, indent=4)
    print(formatted_payload_resp)


extract_data_API()
