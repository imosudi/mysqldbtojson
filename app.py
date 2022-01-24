from mysqltojson import  MysqltoJSON #, flatToCascadedJson
from dbconnect import engine


mysqltojson = MysqltoJSON(engine)
tablelist, tablejson, tablecolumnsjson = mysqltojson.tableData()
#tablesjson = mysqltojson.createDBTableJSON()
print(tablelist, tablejson, tablecolumnsjson)