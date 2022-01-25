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

edit app.py to further custmomize for use   

