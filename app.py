from mysqltojson import  MysqltoJSON #, flatToCascadedJson
from dbconnect import engine


mysqltojson = MysqltoJSON(engine)
### return database schema:
# ddbschemajson = mysqltojson.dbSchema()
ddbschemajson = mysqltojson.dbSchema()


### return all data
# dbdatatojson= mysqltojson.dbData()
dbdata2json= mysqltojson.dbData()



### return database schem and data in :
## db_json/dbname_dbschema.json
## db_json/dbname_completedbdata.json
# jsonfiles =  mysqltojson.jsonfiles()

jsonfiles =  mysqltojson.jsonfiles()


print('README.md is your friend')