# Micropython-esp32

封装了一些Micropython功能性代码，比如`Wi-Fi`,`四驱车`，等等模块。

```python
import wifi

wlan = wifi.connect("wifi名称","密码")

wlan.ifconfig()    # 获取ip信息
wlan.config("mac")
wlan.active(False) # 关闭Wi-Fi

```