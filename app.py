from mysqltojson import  MysqltoJSON #, flatToCascadedJson
from dbconnect import engine


mysqltojson = MysqltoJSON(engine)
#tablelist, tablejson, totalschemaList = mysqltojson.tableData()
tablesjson = mysqltojson.createDBTableJSON()
#print(tablelist, tablejson, totalschemaList) 
print(tablesjson)