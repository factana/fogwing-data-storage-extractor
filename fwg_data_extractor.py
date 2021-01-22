import requests
import json

import urllib3

# Disabled Python warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Data extractor
def data_extractor(username, password, s_date, e_date, dev_eui):
    credentials = {"username": username, "password": password}
    api_key_url = 'https://enterprise.fogwing.net/api/dstorage/getApiKey'
    resp = requests.post(api_key_url, json=credentials, verify=False)
    resp_dict = json.loads(resp.text)

    api_key = resp_dict['token']

    header = {"API-KEY": api_key}
    payload_url = 'https://enterprise.fogwing.net/api/dstorage/getData/{}/{}/{}'.format(dev_eui, s_date, e_date)
    payload_resp = requests.get(payload_url, headers=header, verify=False)
    data = json.loads(payload_resp.text)
    formatted_payload_resp = json.dumps(data, indent=4)
    print("\n*************** Fogwing Data Storage ***************")
    print(formatted_payload_resp)


if __name__ == '__main__':
    # Reading configuration file.
    with open('configuration.json', 'r') as file:
        config = json.load(file)

    # Fogwing Platform credentials reading from configuration file.
    usr_name = config['fwg_platform_cred']['username']
    psw = config['fwg_platform_cred']['password']

    # Fogwing IoTHub credentials reading from configuration file.
    dev_id = config['fwg_IoTHub_cred']['EUI-ID']

    # Duration period of datalog reading from configuration file.
    start_date = config['fetch_data']['start_date']
    end_date = config['fetch_data']['end_date']

    data_extractor(usr_name, psw, start_date, end_date, dev_id)
