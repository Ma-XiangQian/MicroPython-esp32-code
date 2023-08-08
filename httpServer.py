from connectWIFI import connectWIFI
import machine
import socket

pin2 = machine.Pin(2, machine.Pin.OUT)
wifiInfo = connectWIFI("maxiangqian","88888888")

class SocketServer:
    def __init__(this,ip: str,port: int,num: int):
        this.ip = ip
        this.port = port
        this.num = num
        this.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def run(this):
        this.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        this.server.bind((this.ip,this.port))
        this.server.listen(this.num)
        print(f"服务器开启成功啦：{this.ip}:{this.port}")
        while True:
            client = this.server.accept()
            print("有人连接成功！",client[1])
            res = client[0].recv(1024).decode("utf-8")
            if not res:
                client[0].close()
                continue
            header = res.split("\r\n")[0].split(" ")
            body = res.split("\r\n\r\n")[1]
            data =f"{header[2]} 200 ok\r\nAccess-Control-Allow-Origin: *\r\n\r\n{body}"
            if header[0] == "POST":
                if body=="on":
                    pin2.value(1)
                else:
                    pin2.value(0)
                client[0].send(data.encode("utf-8"))
            else:
                fs = open("./index.html","r",encoding="utf-8")
                get_data = f"{header[2]} 200 ok\r\n\r\n{fs.read()}"
                fs.close()
                client[0].send(get_data.encode("utf-8"))
            client[0].close()

s = SocketServer(wifiInfo[0],80,128)
s.run()