# Utils.py
# About:
#    This program reads provides functionality for
#    1. Reading the Config File 
#    2. Creating a DB
#    3. Creating a Document

# Read the config file
import configparser    as cfp
import requests
import json
    
# Get the DB details 
def getDbConn(p_config_file_path):
    
    # Get the config data for the 
    ConfigData = cfp.ConfigParser()
    ConfigData.read(p_config_file_path)

    # l_data = ConfigData['CONNDATA']['url']
    
    # Conn Dictionary
    l_conn_dict = { 'url':ConfigData['CONNDATA']['url']
                   ,'uname':ConfigData['CONNDATA']['uname']
                   ,'passwd':ConfigData['CONNDATA']['passwd']} 

    # Return the dictionary with the connection details
    return l_conn_dict

    

# This method creates a cloudant DB
def createDB(p_db_conn_dict, p_db_name):
    
    l_url       = p_db_conn_dict.get('url')
    l_user_name = p_db_conn_dict.get('uname')
    l_user_pass = p_db_conn_dict.get('passwd')
    
    
    print(l_url+p_db_name, l_user_name, l_user_pass)

    requests.put(l_url+p_db_name, auth=(l_user_name, l_user_pass))



# This method creates a cloudant DB Document with data
def createData(p_db_conn_dict, p_db_name, p_coll_name, p_document):
    
    l_url       = p_db_conn_dict.get('url')
    l_user_name = p_db_conn_dict.get('uname')
    l_user_pass = p_db_conn_dict.get('passwd')
    
    print('createData')
    print(l_url + p_db_name + '/' + p_coll_name)
    
    # Create another document:
    requests.put(l_url + p_db_name + '/' + p_coll_name,
                 auth=(l_user_name, l_user_pass),
                 headers={"content-type":"application/json"},
                 data=json.dumps(p_document))



# This method reads the cloudant db data                 
def readData(p_db_conn_dict, p_db_name, p_coll_name):

    l_url       = p_db_conn_dict.get('url')
    l_user_name = p_db_conn_dict.get('uname')
    l_user_pass = p_db_conn_dict.get('passwd')
    
    # print('readData')
    # print(l_url + p_db_name + '/' + p_coll_name)
    
    # Get a document:
    r = requests.get(l_url + p_db_name + '/' + p_coll_name,
                 auth=(l_user_name, l_user_pass))
                     
    return r.text
    

    
# This method checks if the target key-value exists in a Dict or not
def checkData(p_src_dict, p_key, p_value):

	# Convert string:p_src_dict into dict
    l_dict_str = p_src_dict
    json_acceptable_string = l_dict_str.replace("'", "\"")
	
	# Final dict is l_dict
    l_dict = json.loads(json_acceptable_string)

    if (p_key, p_value) in l_dict.items():
        return "Data " + p_value + " Success"
    else:
        return "Data " + p_value + " Failed"
