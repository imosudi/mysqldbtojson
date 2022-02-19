from mysqltojson import  MysqltoJSON #, flatToCascadedJson
from dbconnect import engine


mysqltojson = MysqltoJSON(engine)


### return database facts; viz: list of tables and diction of 
#tablenames as keys and lists corresponding column names as values 
dbtableList, dbtableListDict, schemaList = mysqltojson.dbfacts()


### return database schema:
# ddbschemajson = mysqltojson.dbSchema()
ddbschemajson = mysqltojson.dbSchema()


### return all data
# dbdatatojson= mysqltojson.dbData()
dbdata2json= mysqltojson.dbData()



### return database schem and data in :
## db_json/dbname_dbschema.json
## db_json/dbname_completedbdata.json
# jsonfiles =  mysqltojson.jsonFiles()

jsonfiles =  mysqltojson.jsonFiles()


print('README.md is your friend')
