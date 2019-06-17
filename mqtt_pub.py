import paho.mqtt.subscribe as subscribe

import time
import paho.mqtt.client as paho
# broker="broker.hivemq.com"
broker="192.168.43.251"
#define callback


client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
# client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
# print("subscribing ")
# client.subscribe("house/bulb1")#subscribe
time.sleep(2)

# print("publishing ")
l=""
while l!="stop":
	l=input("Enter massage to publish:")
	client.publish("led",l)#publish
	time.sleep(1)
#client.disconnect() #disconnect
client.loop_stop() #stop loop