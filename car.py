from machine import Pin,PWM

class Car:
    def __init__(this,wheels: list,freq: int):
        this.a1 = PWM(Pin(wheels[0][0]),freq=freq,duty=0)
        this.a2 = PWM(Pin(wheels[0][1]),freq=freq,duty=0)
        this.b1 = PWM(Pin(wheels[1][0]),freq=freq,duty=0)
        this.b2 = PWM(Pin(wheels[1][1]),freq=freq,duty=0)
        this.c1 = PWM(Pin(wheels[2][0]),freq=freq,duty=0)
        this.c2 = PWM(Pin(wheels[2][1]),freq=freq,duty=0)
        this.d1 = PWM(Pin(wheels[3][0]),freq=freq,duty=0)
        this.d2 = PWM(Pin(wheels[3][1]),freq=freq,duty=0)
        this.status="stop"
        this.all = [this.a1,this.a2,this.b1,this.b2,this.c1,this.c2,this.d1,this.d2]
    def forward(this):
        this.stop()
        this.status="forward"
        this.a2.duty(int(1023*1))
        this.b1.duty(int(1023*1))
        this.c2.duty(int(1023*1))
        this.d1.duty(int(1023*1))
    def retreat(this):
        this.stop()
        this.status="retreat"
        this.a1.duty(int(1023*1))
        this.b2.duty(int(1023*1))
        this.c1.duty(int(1023*1))
        this.d2.duty(int(1023*1))
    def left(this):
        this.a2.duty(int(1023*0.3))
        this.b1.duty(int(1023*1))
        this.c2.duty(int(1023*0.3))
        this.d1.duty(int(1023*1))
    def right(this):
        this.a2.duty(int(1023*1))
        this.b1.duty(int(1023*0.3))
        this.c2.duty(int(1023*1))
        this.d1.duty(int(1023*0.3))
    def turnLeft(this):
        this.stop()
        this.status="turnLeft"
        this.a1.duty(int(1023*0.8))
        this.b1.duty(int(1023*0.8))
        this.c1.duty(int(1023*0.8))
        this.d1.duty(int(1023*0.8))
    def turnRight(this):
        this.stop()
        this.status="turnRight"
        this.a2.duty(int(1023*0.8))
        this.b2.duty(int(1023*0.8))
        this.c2.duty(int(1023*0.8))
        this.d2.duty(int(1023*0.8))
    
    def stop(this):
        this.status="stop"
        for g in this.all:
            g.duty(0)
            

class Mecanum(Car):
    def left(this):
        this.stop()
        this.b1.duty(int(1023*1))
        this.d2.duty(int(1023*1))
        this.a1.duty(int(1023*1))
        this.c2.duty(int(1023*1))
    def right(this):
        this.stop()
        this.a2.duty(int(1023*1))
        this.c1.duty(int(1023*1))
        this.b2.duty(int(1023*1))
        this.d1.duty(int(1023*1))
    def turnLeft(this):
        this.stop()
        this.a1.duty(int(1023*1))
        this.c1.duty(int(1023*1))
        this.b1.duty(int(1023*1))
        this.d1.duty(int(1023*1))
    def turnRight(this):
        this.stop()
        this.a2.duty(int(1023*1))
        this.c2.duty(int(1023*1))
        this.b2.duty(int(1023*1))
        this.d2.duty(int(1023*1))