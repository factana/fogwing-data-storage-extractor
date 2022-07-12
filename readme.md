# _Fogwing python Integration to Extract data from Data Storage using API_

This directory provide three files that extract all data from 
Fogwing data storage using API.

**Note that these SDKs are currently in preview and are subject to change.**

## Fogwing IoT data extractor
we have provided three files:
* [fwg_data_extractor.py](https://github.com/factana/fogwing-data-storage-extractor/blob/master/fwg_data_extractor.py)
* [configuration.json](https://github.com/factana/fogwing-data-storage-extractor/blob/master/configuration.json)
* [requirements.txt](https://github.com/factana/fogwing-data-storage-extractor/blob/master/requirements.txt)

The logic behind the code is to extract all data from Fogwing data storage,
between selected duration using API client call.
Results are in json string.

## Step:1
### Required files
* Copy all the provided files into your Rasberry Pi and you are good to start ! You now finish with coding part.

## Step:2
### Installing the libraries
* Install all required libraries using pip with our requirements.txt file.
    ```
    pip install -r requirements.txt
    ```
  
## Step:3
###  Credentials
**Note:-** Do the following modification in **configuration.json** file.
* Change the **username** and **password** with your Fogwing Platform
  credentials. 
* Change the **dev_eui** with your Fogwing IoTHub access credentials. 
* Enter the **start_date** and **end_date** to extract all the data from 
  Fogwing data storage in **DD-MM-YYYY** format.
  
  
 ## Step:4
 ### Run and Get Started to Extract data from Fogwing data storage
* Now run the file with the below command.
    ```
    python fwg_data_extractor.py
    ```
  **Note:-** Provided everything goes in line with the above mentioned instructions,
         you will be able to see all the data in command line.

 ### Getting help and finding Fogwing docs
 * [Fogwing Platform Forum](https://enterprise.fogwing.net/)
 * [Fogwing Platform Docs](https://docs.fogwing.io/)
 * Please visit https://www.fogwing.io/industrial-iot-platform/ for more information about Fogwing Industrial IoT Platform.
