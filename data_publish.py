import paho.mqtt.client as mqtt
from time import sleep
from random import uniform
from flask import Flask,render_template
app = Flask(__name__)

latitude = 12.95677
longitude = 77.73164

ORG = "pn74op"
DEVICE_TYPE = "PC" 
TOKEN = "wafMPutb(X-wubBR?9"
DEVICE_ID = "10001"

#host = "pn74op.messaging.internetofthings.ibmcloud.com"
#clientId = "d:pn74op:PC:10001"
#username = "use-token-auth"
#password = "wafMPutb(X-wubBR?9"
#topic = "iot-2/evt/status/fmt/json";

server = ORG + ".messaging.internetofthings.ibmcloud.com"
topicTemp = "iot-2/evt/temperature/fmt/json"
topicLatitude = "iot-2/evt/latitude/fmt/json"
topicLongitude = "iot-2/evt/longitude/fmt/json"
authMethod = "use-token-auth"
token = TOKEN
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID

mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)

def takeMeToHospital(temp,lat,lng):
    #print("Values:",lat,lng,temp)    
    @app.route('/')
    def map_func():
        return render_template('map.html', lat=lat,lng=lng,temp=temp)
    
while True:
    temperature = uniform(96.0,101.0)
    mqttc.publish(topicTemp, temperature)
    mqttc.publish(topicLatitude, latitude)
    mqttc.publish(topicLongitude, longitude)
    print ("Published: " + "%s;%s/%s "%(temperature,latitude,longitude))
    if(temperature>=99.1 or temperature<=96.9):
        print("Need attention!")
        takeMeToHospital(temperature,latitude,longitude)
        break
    sleep(2)

mqttc.loop()

if __name__ == '__main__':
    app.run(debug = True) 