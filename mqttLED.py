import wifi
from umqttsimple import MQTTClient
from machine import Pin

pin2 = Pin(2,Pin.OUT,value=0)

wlan = wifi.connect("CMCC-马云龙","myl12345")

client = MQTTClient("esp32","192.168.10.74",1883,user="admin",password="admin")
def sub(topic,msg):
    topic = topic.decode("utf-8")
    msg = msg.decode("utf-8")
    if msg == "on":
        pin2.on()
    else:
        pin2.off()

client.set_callback(sub)
client.connect()
client.subscribe(b"led")
while True:
    client.check_msg()
    
