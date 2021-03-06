from unicodedata import name
from dbconnect import engine, alchemyencoder
import json, os
from sqlalchemy import inspect

#dbname = engine.url.database

"""class MysqltoJSON(object):
    def __init__(self, engine, *args):
        super(MysqltoJSON, self).__init__(*args)
        self.engine = engine;       inspector = inspect(engine)
        self.inspector = inspector; self.dbname = str(engine.url.database)

    def dbfacts(self):
        dbtableList = [];   schemaList = [];  inspector = self.inspector;   
        
        for table_name in inspector.get_table_names():
            dbtableList.append(table_name)
            columnList = [];    columnDict  = {};   columnDict['name']  = table_name
            
            for column in inspector.get_columns(table_name):
                columnList.append(column['name']);  columnDict['columns']  =  columnList
            
            schemaList.append(columnDict)
        #schemasDict = dict(dbname = dbtableList) #dbtables 
        return dbtableList, schemaList"""
        
class MysqltoJSON(object):
    def __init__(self, engine, *args):
        super(MysqltoJSON, self).__init__(*args)
        self.engine = engine;       inspector = inspect(engine)
        self.inspector = inspector; self.dbname = str(engine.url.database)

    def dbfacts(self):
        dbtableList = [];   schemaList = [];  inspector = self.inspector;   dbtableListDict = {};
        dbname = self.dbname
        
        for table_name in inspector.get_table_names():
            dbtableList.append(table_name)
            columnList = [];    columnDict  = {};   columnDict['name']  = table_name
                        
            for column in inspector.get_columns(table_name):
                columnList.append(column['name']);  columnDict['columns']  =  columnList
                        
            schemaList.append(columnDict)
            dbtableListDict[table_name] = columnList
        #schemasDict = dict(dbname = dbtableList) #dbtables 
        return dbtableList, dbtableListDict, schemaList  
          
    def dbSchema(self):
        dbname = self.dbname
        schemasDict = {};   schemasDict['database'] = dbname
        schemasDict['drivername']    = engine.url.drivername       
        schemasDict['host']          = engine.url.host
        schemasDict['password']      = engine.url.password
        dbtableList, dbtableListDict, schemaList = self.dbfacts()
        self.dbtableList = dbtableList
        schemasDict['tables']   = schemaList
        dbschemajson            = json.dumps(schemasDict, default=alchemyencoder, indent=2)
        #return dbtableList, schemaList, dbschemajson 
        return dbschemajson

    def dbData(self):
        engine = self.engine
        #dbtableList, schemaList, tablesjson = self.tableData()
        dbtableList, dbtableListDict, schemaList = self.dbfacts()
        #dbtableList
        completedbDataList = []
        dbdataDict = {}
        
        for dbtable in dbtableList :
            dbtableData     = engine.execute('SELECT * FROM {dbtable}' .format(dbtable=dbtable))
            dbdataList      = [row for row in dbtableData]
            dbtableDataList = []
            
            for row in dbdataList :
                #print( { dbtable : dict(row) }, 
                #      '\n')
                #print( dict(row))
                dbtableDataList.append(dict(row)) 
                dbtableDataDict = {dbtable : dbtableDataList}
                
            dbdataDict[dbtable] = dbdataList
            completedbDataList.append(dbtableDataDict)
        
        completedbdatajson = json.dumps([dict(row) for row in completedbDataList], default=alchemyencoder, indent=2)
        return completedbdatajson
    
    
    def dbtablePropertyDict(self):
        dbtableList, dbtableListDict, schemaList = self.dbfacts()
        dbtablePropertyList = [];	dbtablePropertyDict = {}
        for dbtable in dbtableList :
            table_columns = engine.execute('SHOW FIELDS FROM {table_name}'.format(table_name=dbtable)) 
            table_columns = [list(items) for items in table_columns]
            
            dbtablePropertyDict[dbtable] = table_columns
            dbtablePropertyList.append(dbtablePropertyDict)
        dbtablePropertyjson = json.dumps([dict(row) for row in dbtablePropertyList], default=alchemyencoder, indent=2)
        return dbtablePropertyjson
       
    def jsonFiles(self):
        dbschemajson = self.dbSchema()
        dbtablePropertyjson = self.dbtablePropertyDict()
        completedbdatajson  = self.dbData()
        pwd                 = os.path.dirname(os.path.abspath(__file__))
        
        if not os.path.exists(f'{pwd}/db_json/') :
            os.makedirs(f'{pwd}/db_json/')
        
        with open(f'db_json/{self.dbname}_dbschema.json', 'w+') as file :
            file.write(dbschemajson)
        file.close()
        
        with open(f'db_json/{self.dbname}_dbtableProperty.json', 'w+') as file :
            file.write(dbtablePropertyjson)
        file.close()
        
        with open(f'db_json/{self.dbname}_completedbdata.json', 'w+') as file :
            file.write(completedbdatajson)
        file.close()
            
        return f'{pwd}/db_json/{self.dbname}_dbschema.json',\
            f'{pwd}/db_json/{self.dbname}_completedbdata.json'
