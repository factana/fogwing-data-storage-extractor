""" * Copyright (C) 2023 Factana Computing Pvt Ltd.
    * All Rights Reserved.
    * This file is subject to the terms and conditions defined in
    * file 'LICENSE', which is part of this source code package."""

import requests
import json

# Load the credentials
with open('configuration.json', 'r') as cred_file:
    cred = json.loads(cred_file.read())

config = cred.get("FW_CRED")
apikey = config.get("API_KEY")
e_eui = config.get("EDGE_EUI")
acc_id = config.get("ACCOUNT_ID")

date_range = cred.get("DATE_RANGE")
s_date = date_range.get("START_DATE")
e_date = date_range.get("END_DATE")


def data_extractor():
    """
    This function is to Extract data from Fogwing using API Key.
    :returns: API Response
    :rtype: json
    """
    params = {"apiKey": apikey, "edgeEUI": e_eui, "startDate": s_date, "endDate": e_date, "accountID": acc_id}
    api_key_url = 'https://api.fogwing.net/api/v1/dstorage/getData/withApiKey'
    api_resp = requests.get(api_key_url, params=params, verify=True)
    data = json.loads(api_resp.text)
    formatted_payload_resp = json.dumps(data, indent=4)
    return formatted_payload_resp


if __name__ == '__main__':
    print("\n*************** Fogwing Data Storage ***************")
    print(data_extractor())
