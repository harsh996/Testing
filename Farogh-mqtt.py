
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
#from socketIO_client import SocketIO, BaseNamespace
import http.client,urllib.parse
from random import randint
# Subscribing to the topic "temp"
#def on_connect(client, userdata, flags, rc):
 # print(str(client)+'\n'+str(userdata))
  #print("Connected with result code "+str(rc))



#def on_message(client, userdata, msg):
 #      print("Message arrived from "+str(client))
  #     print(msg.topic+" "+str(msg.payload))
       
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass


client = mqtt.Client()
x=client.connect("192.168.0.167",1883,60)
#	client.on_connect = on_connect
#	client.on_message = on_message
client.on_publish = on_publish
while 1:
	data=randint(1,100)	
	data2=randint(1,100)
	data3=randint(1,40)
	data4=randint(1,79)
	client.publish("9/MB/EM/0/2/KW",data)
	client.publish('9/MB/EM/0/2/PF',data2)
	client.publish('9/MB/EM/0/2/KVAH',data3)
	client.publish('9/MB/EM/0/2/KVA',data4)
	client.publish()


	time.sleep(15)
	
	
#Publish to the topic "temp/led"


def server_responded(*body):
    print ('response'),body
#emit_data = {
#  'method' : 'post',
#  'url': '/device',

#client.loop_forever()

