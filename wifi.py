import network
    
def connect(name: str,password: str):
    # 设置Wi-Fi
    wlan = network.WLAN(network.STA_IF)
    # 开启Wi-Fi
    wlan.active(True)
    # Wi-Fi列表
    wlanList = []
    # 获取附近Wi-Fi
    for w in wlan.scan():
        wlanList.append(w[0].decode("utf-8"))
    # 判断附近是否有该Wi-Fi
    if wlanList.count(name):
        # 连接Wi-Fi
        wlan.connect(name,password)
        # 等待连接成功！
        while not wlan.isconnected():
            pass
        # 判断Wi-Fi是否连接成功
        if wlan.isconnected():
            print(f"Wi-Fi: {name} 连接成功！")
        else:
            print(f"Wi-Fi: {name} 连接失败！")
    else:
        print(f"Wi-Fi: {name} 没有信号！")
    return wlan
        
        
        


        
    