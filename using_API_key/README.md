
# **_Extracting Data from Fogwing IIoT Data Storage using Python and API Key_**
This repository contains three files that enable you to extract data from Fogwing IIoT using API Key.

>**Note:** This SDK is subject to change as it is currently in preview.

## **Fogwing IIoT data extractor**

To extract data from Fogwing using an API Key, you will need to download the following files:
* [fw_data_ext_apikey.py](https://github.com/factana/fogwing-data-storage-extractor/blob/master/using_API_key/fwg_data_extractor.py)
* [configuration.json](https://github.com/factana/fogwing-data-storage-extractor/blob/master/using_API_key/configuration.json)
* [requirements.txt](https://github.com/factana/fogwing-data-storage-extractor/blob/master/using_API_key/requirements.txt)

>**Note:** The purpose of the code is to extract data from Fogwing IIoT using an API client. To achieve this, you can modify the **configuration.json** file to configure the Fogwing IoTHub credentials and Date range.

## Here are the steps to follow in order to extract data from Fogwing IIoT using an API Key:

### **1. Moving Files.**
* Move downloaded files to a directory of your choice on your system. Once you have done this, you can proceed with the next steps.

### **2. Installing Libraries**
* You can install all the required libraries using pip and the requirements.txt file provided using follwing command.

  - `pip install -r requirements.txt`

### **3. Update Credentials**
To update credentials for Fogwing IoTHub access, you need to modify the **configuration.json** file.
* Replace the placeholder values of **API_KEY** and **ACCOUNT_ID** with API Key and Account ID of Fogwing account.
* Replace the placeholder values of **EDGE_EUI** with the specific Edge EUI of the Edge device from which you wish to extract data.
* Replace the placeholders **START_DATE** and **END_DATE** with the specific dates that define the range of data you wish to extract.

>**Note:** The date range needs to be entered in the format of **DD-MM-YYYY** and should not exceed a duration of **three months**.  

### **4. Run the Program and Get Started with Fogwing IIoT**
* To run the program, use the following command.
   - `python fw_data_ext_apikey.py`


>**Note:** If everything goes according to the instructions mentioned above, you should see `"statusCode": 200, "message": "OK", "description": "The Request Has Succeeded","data": [{....}]` message displayed on the Terminal.


## **Where to Find Help and Resources for Fogwing**
* [Fogwing Open APIs Docs.](https://api.fogwing.net/)
* [Fogwing Platform Forum.](https://community.fogwing.io/)
* [Fogwing Platform Docs.](https://docs.fogwing.io/)


## Please visit https://www.fogwing.io/industrial-iot-platform/ for more information about Fogwing Industrial IoT Platform. ##
