import umqtt.simple

class MQTTClient():
    def __init__(this,id: str,host: str,port: int=0,user=None,password=None,keepalive=0,ssl=False,ssl_params={}):
        this.client = umqtt.simple.MQTTClient(id,host,port,user,password,keepalive,ssl,ssl_params)
        this.host = host
        this.id = id
        this.port = port
        this.topics = []
        this.sub_func = {}
        this.isconnected = False
    def connect(this):
        this.client.connect()
        this.isconnected = True
        print(f"MQTT:{this.host}:{this.port} 连接成功！")
        for t in this.topics:
            this.client.subscribe(t)
        return this.message
    def subscribe(this,topic: str):
        this.topics.append(bytes(topic,"utf-8"))
        def outer(target):
            this.sub_func[topic]=target
            def callback(topic,msg):
                this.sub_func[topic.decode("utf-8")](msg.decode("utf-8"))
            this.client.set_callback(callback)
            return
        return outer
    def disconnect(this):
        this.isconnected = False
        this.client.disconnect()
    def publish(this,topic,msg,retain=False,qos=0):
        this.client.publish(bytes(topic,"utf-8"),bytes(msg,"utf-8"),retain,qos)
    def wait_msg(this):
        this.client.wait_msg()
    def check_msg(this):
        this.client.check_msg()
    def message(this):
        while this.isconnected:
            this.wait_msg()