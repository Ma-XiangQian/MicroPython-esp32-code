import wifi
from umqttsimple import MQTTClient
from machine import Pin
import car

pin2 = Pin(2,Pin.OUT,value=0)

wlan = wifi.connect("CMCC-马云龙","myl12345")
pin2.on()

client = MQTTClient("esp32","192.168.10.74",1883,user="admin",password="admin")

def sub(topic,msg):
    topic = topic.decode("utf-8")
    msg = msg.decode("utf-8")
    if msg == "stop":
        car.stop()
    elif msg=="forward":
        car.forward()
    elif msg=="retreat":
        car.retreat()
    elif msg=="left":
        car.left()
    elif msg=="right":
        car.right()
    elif msg=="x_right":
        car.x_right()
    elif msg=="x_left":
        car.x_left()
    else:
        car.stop()
    
client.set_callback(sub)
client.connect()
client.subscribe(b"car")
while True:
    client.check_msg()
