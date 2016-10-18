# db_createNtest_data.py
# About:
#    This program reads the database config and creates the data
#     

import Utils


# List of Collection
l_document      = ["docx1", "docx2", "docx3"]
l_document_data = [{"Set1":"ABC"}, {"Set2":"PQR"}, {"Set3":"XYZ"}]


# Run the Program    
l_config_file_path = "C:\\codeChallenge\\conn.config"

# Create Conn Dictionary from the Utils file's getDbConn method
l_db_conn_dict = Utils.getDbConn(l_config_file_path)

# Some DB Name
l_db_name      = 'mydb'



# Create the DB only once
Utils.createDB(l_db_conn_dict, l_db_name)



# Create the Data
# Loop through the list of values
for h in range(len(l_document)):
    
    # This method creates a cloudant DB Document with data
    Utils.createData(l_db_conn_dict, l_db_name, str(l_document[h]), l_document_data[h])
    

# Check to see if the data is created
for i in range(len(l_document)):
    
    # This method creates a cloudant DB Document with data
    print(Utils.readData(l_db_conn_dict, l_db_name, str(l_document[i])))
    
    
    # Extract Key and Value from the List of Dictionaries of the document_data
    for p_key, p_value in l_document_data[i].items():
    
        # Check the Success or failure
        print(Utils.checkData(Utils.readData(l_db_conn_dict, l_db_name, str(l_document[i])), p_key, p_value))
