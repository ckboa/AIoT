from flask import Flask
from flask_mysqldb import MySQL
from flask import jsonify
from flask import flash, request 
from datetime import datetime

app = Flask(__name__)

#mySQL Config 
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'yourdatabase'

# init MYSQL
mysql = MySQL(app)

# add dht data   
@app.route('/sensor_dht', methods=['POST'])
def sensor_dht():
    try: 
       details = request.json 
       temperature = details['temp']
       huminity = details['humi']
       current = datetime.now()
       day = current.strftime("%Y-%m-%d")
       time = current.strftime("%H:%M:%S")
       cur = mysql.connection.cursor()      
       cur.execute("INSERT INTO sensor_dht(temperature, huminity, Date, Time) VALUES (%s, %s, %s, %s)", \
           (temperature, huminity, day, time))
       mysql.connection.commit()
       cur.close()
       resp = jsonify("Data Added")
       resp.status_code = 200
       return resp 
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(debug=True)
