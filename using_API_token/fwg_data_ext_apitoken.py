import requests
import json

# Reading configuration file.
with open('configuration.json', 'r') as cred_file:
    cred = json.loads(cred_file.read())

config = cred.get("FW_CRED")
username = config.get("USERNAME")
password = config.get("PASSWORD")
e_eui = config.get("EDGE_EUI")

data_range = cred.get("DATE_RANGE")
s_date = data_range.get("START_DATE")
e_date = data_range.get("END_DATE")


def get_APItoken():
    """
    This function is to generate API token.
    :returns: API Token
    :rtype: String
    """
    credentials = {"username": username, "password": password}
    api_token_url = "https://api.fogwing.net/api/v1/dstorage/getApiToken"
    resp = requests.post(api_token_url, json=credentials, verify=True)
    resp_dict = json.loads(resp.text)
    return resp_dict.get("data").get("token")


def data_extractor():
    """
    This function is to Extract data to Fogwing.
    :returns: API Response
    :rtype: json
    """
    header = {"Authorization": f"Bearer {get_APItoken()}"}
    data_ext_url = f"https://api.fogwing.net/api/v1/dstorage/getData/withApiToken/{e_eui}/{s_date}/{e_date}"
    request_resp = requests.get(data_ext_url, headers=header, verify=True)
    data = json.loads(request_resp.text)
    formatted_api_resp = json.dumps(data, indent=4)
    return formatted_api_resp


if __name__ == '__main__':
    print("\n*************** Fogwing Data Storage ***************")
    print(data_extractor())
