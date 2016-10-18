PYTHON Assignment
-----------------
Config File to hold the details of the cloudant URL, User, Pass


# utils.py file
This file has the methods 

**getDbConn**
This creates the DB Conn Dictionary with the URL, USER, PASS
Accepts the config File location as the input
Returns a Dictionary with URL, USER, PASS

    
**createDB**
This method Creates a DB, Accepts the connection details dictionary and the DB name
and creates a DB


**createData**
This method Creates a DB, Accepts the connection details dictionary and the DB name, collection name and the document data
as inputs and creates the data in the DB specified

    
**readData**    
This method Creates a DB, Accepts the connection details dictionary and the DB name, collection name and returns the document data


# The db_createNtest
creates the DB, Data and tests if the data is created properly or not.
