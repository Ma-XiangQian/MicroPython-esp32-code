import bluetooth
from machine import Timer,Pin

led = Pin(2,Pin.OUT,value=0)
tim = Timer(0)

ble = bluetooth.BLE()
ble.active(True)
name = "ESP32-不熬夜"
ble.config(gap_name=name)

# 蓝牙中断
def bt_irq(event,data):
    if event==1:
        print("连接成功！")
        connected()
    elif event==2:
        print("断开连接！")
        disconnected()
        advertise()
    elif event==3:
        tx,rx=data
        buf = ble.gatts_read(rx)
        print(buf.decode("utf-8"))
        ble.gatts_notify(0,txx,'Hello,eps32')

ble.irq(bt_irq)
        
# 断开连接事件函数
def disconnected():
    tim.init(period=200,mode=Timer.PERIODIC, callback=lambda t:led.value(not led.value()))
# 连接成功事件函数
def connected():
    tim.deinit()
    led.on()
# 广播信号
def advertise():
    # 设备标识
    flag = b"\x02\x01\x06"
    # 设备名称 utf-8
    nameByte = name.encode("utf-8")
    lenght = bytearray((len(nameByte) + 1, 0x09))
    adv_data = flag+lenght+ nameByte
    print(adv_data)
    ble.gap_advertise(100,adv_data=adv_data)

# 注册服务
SERVER_1_UUID = bluetooth.UUID(0x9011)
#创建特性并设置特性的读写权限
UART_RX = (bluetooth.UUID(0x9012), bluetooth.FLAG_READ | bluetooth.FLAG_WRITE, )
UART_TX = (bluetooth.UUID(0x9013), bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY, )
SERVER_1 = (SERVER_1_UUID, (UART_RX , UART_TX, ) , )
SERVICES = (SERVER_1, )
((rx,txx), ) = ble.gatts_register_services(SERVICES) #注册服务到gatts

disconnected()
advertise()

def buttons_irq(pin):
    ble.gatts_notify(0,txx,'远方传来风笛👀')
btn = Pin(0,Pin.IN)
btn.irq(trigger=Pin.IRQ_FALLING, handler=buttons_irq)