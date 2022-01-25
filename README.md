# mysqldbtojson
# Clone this repo:  

 git clone https://github.com/imosudi/mysqldbtojson.git    

 cd mysqldbtojson

# create .env file with the  target database details:    

 #DB_HOST="localhost"    
 DB_HOST="xxxxxxx.xxxxxxxorIP"   
 DB_USER="dbuser"    
 DB_PASS="dbpassword"    
 DB_NAME="dbname"    

# Create Python virtual environment :   

python3 -m venv venv    
. venv/bin/activate 

python app

Edit app.py to further custmomize for use   
# Create object instance    
 mysqltojson = MysqltoJSON(engine)  

# return database schema:
 ddbschemajson = mysqltojson.dbSchema()

# return all data
 dbdata2json= mysqltojson.dbData()

# return database schema and data json files in db_json/ :
 jsonfiles =  mysqltojson.jsonfiles()

# run

 python app.py  
 