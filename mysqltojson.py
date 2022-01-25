from unicodedata import name
from dbconnect import engine, alchemyencoder
import json, os
from sqlalchemy import inspect

#dbname = engine.url.database

class MysqltoJSON(object):
    def __init__(self, engine, *args):
        super(MysqltoJSON, self).__init__(*args)
        self.engine = engine;       inspector = inspect(engine)
        self.inspector = inspector; self.dbname = str(engine.url.database)

    
    def tableData(self):
        dbtableList = [];   schemaList = [];  inspector = self.inspector;    dbname = self.dbname
        schemasDict = {};   schemasDict['database'] = dbname
        schemasDict['drivername']    = engine.url.drivername       
        schemasDict['host']          = engine.url.host
        schemasDict['password']      = engine.url.password
        
        for table_name in inspector.get_table_names():
            dbtableList.append(table_name)
            columnList = [];    columnDict  = {};   columnDict['name']  = table_name
            
            for column in inspector.get_columns(table_name):
                columnList.append(column['name']);  columnDict['columns']  =  columnList
            
            schemaList.append(columnDict)
        #schemasDict = dict(dbname = dbtableList) #dbtables 
        
        self.dbtableList = dbtableList
        schemasDict['tables']   = schemaList
        dbschemajson            = json.dumps(schemasDict, default=alchemyencoder, indent=2)
        #return dbtableList, schemaList, dbschemajson 
        return dbschemajson
    

    def createDBTableJSON(self):
        engine = self.engine
        #dbtableList, schemaList, tablesjson = self.tableData()
        dbtableList = self.dbtableList
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
    

    def jsonfiles(self):
        dbschemajson = self.tableData()
        completedbdatajson  = self.createDBTableJSON()
        pwd                 = os.path.dirname(os.path.abspath(__file__))
        
        if not os.path.exists(f'{pwd}/db_json/') :
            os.makedirs(f'{pwd}/db_json/')
        
        with open(f'db_json/{self.dbname}_dbschema.json', 'w+') as file :
            file.write(dbschemajson)
        file.close()
        
        with open(f'db_json/{self.dbname}_completedbdata.json', 'w+') as file :
            file.write(completedbdatajson)
        file.close()
            
        return f'{pwd}/db_json/{self.dbname}_dbschema.json',\
            f'{pwd}/db_json/{self.dbname}_completedbdata.json'
