from machine import Pin

a1 = Pin(15,Pin.OUT,value=0)
a2 = Pin(21,Pin.OUT,value=0)

b1 = Pin(4,Pin.OUT,value=0)
b2 = Pin(16,Pin.OUT,value=0)

c1 = Pin(13,Pin.OUT,value=0)
c2 = Pin(12,Pin.OUT,value=0)

d1 = Pin(18,Pin.OUT,value=0)
d2 = Pin(19,Pin.OUT,value=0)

wheels = [a1,a2,b1,b2,c1,c2,d1,d2]

def stop():
    for w in wheels:
        w.off()


def forward():
    stop()
    a2.on()
    b1.on()
    c2.on()
    d1.on()
    
def retreat():
    stop()
    a1.on()
    b2.on()
    c1.on()
    d2.on()
    
def x_right():
    stop()
    a2.on()
    c1.on()
    b2.on()
    d1.on()
    
def x_left():
    stop()
    b1.on()
    d2.on()
    a1.on()
    c2.on()
    
def right():
    stop()
    a2.on()
    c2.on()
    b2.on()
    d2.on()
    
def left():
    stop()
    a1.on()
    c1.on()
    b1.on()
    d1.on()
    
    
    
    