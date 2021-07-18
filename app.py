import sqlite3
from flask import request, jsonify

# SQLITE connection
conn = sqlite3.connect('yellow_taxi_data.db')
cur = conn.cursor()

#Intialize Flask app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Get method for root
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Yellow taxi data</h1>
<p>Data for NYC yellow taxi</p>'''

#Get method to retrive maximum tip per quarter
@app.route('/api/tip/2020/<int:quarter_number>/max', methods=['GET'])
def get_max_tip_quarter(quarter_number):
    return jsonify({ "maxTipPercentage": cur.execute('SELECT max(tip_percent) FROM yellow_taxi_data where quarter=quarter_number')    })

#Get method to retrive maximum tip per year
@app.route('/api/tips/2020/max', methods=['GET'])
def get_max_tip_year():
    return jsonify({ "maxTipPercentage": [{"quarter": 1,"maxTipPercentage": cur.execute('SELECT max(tip_percent) FROM yellow_taxi_data where quarter=1)}
    ,{ "maxTipPercentage": [{"quarter": 1,"maxTipPercentage": cur.execute('SELECT max(tip_percent) FROM yellow_taxi_data where quarter=2)}
    ,{ "maxTipPercentage": [{"quarter": 1,"maxTipPercentage": cur.execute('SELECT max(tip_percent) FROM yellow_taxi_data where quarter=3)}
    ,{ "maxTipPercentage": [{"quarter": 1,"maxTipPercentage": cur.execute('SELECT max(tip_percent) FROM yellow_taxi_data where quarter=4}]})

#Get method to retrive maximum speed per hour
@app.route('/api/speed/<int:year>/<int:month>/<int:day>/max', methods=['GET'])
def get_max_tip_year():
    date_value=day+'-'+month+'-'+year
    results = cur.execute('SELECT hour,max(speed) as maxSpeed FROM yellow_taxi_data where CONVERT(VARCHAR(10), tpep_dropoff_datetime, 105)=  group by hour')
    return jsonify({ "tripSpeeds": [results]})
app.run()