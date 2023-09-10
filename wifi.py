import network
    
def connect(name: str,password: str,callback=None):
    # 设置Wi-Fi
    wlan = network.WLAN(network.STA_IF)
    # 开启Wi-Fi
    wlan.active(True)
    # Wi-Fi列表
    wlanList = []
    # 获取附近Wi-Fi
    for w in wlan.scan():
        w = w[0].decode("utf-8")
        if w:
            wlanList.append(w)
    # 判断Wi-Fi信号
    # if not name in wlanList:
    #     print(f"Wi-Fi: {name} 不在服务区！")
    #     return wlan
    # 判断是否连接Wi-Fi
    if wlan.isconnected():
        if wlan.config("essid") in wlanList:
            if callback:
                callback()
            print(f"Wi-Fi: {wlan.config('essid')} 连接成功！")
            return wlan
    # 连接Wi-Fi
    wlan.disconnect()
    wlan.connect(name,password)
    while not wlan.isconnected():
        pass
    if callback:
        callback()
    print(f"Wi-Fi: {wlan.config('essid')} 连接成功！")
    return wlan