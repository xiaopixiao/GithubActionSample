import os
import urllib.parse
from time import sleep

log_file_path = r'C:\Users\Administrator\Desktop\charge.log'

variable_name = '"channelMap"'
variable_value = None
name_value = None

start = '"channelMap":'
end = ',"returnCode"'
start_name = '"deviceName":"'
end_name = '","userId"'

def run():
    if not os.path.exists(log_file_path):
        print('no log file')
    else:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # 去除行尾的换行符
                line = line.strip()
                # 检查行是否包含目标变量名
                if line.startswith('details = {') and variable_name in line:
                    # 提取变量值
                    start_index = line.find(start) + len(start)
                    end_index = line.find(end, start_index)
                    variable_value = line[start_index:end_index]
                    start_index_name = line.find(start_name) + len(start_name)
                    end_index_name = line.find(end_name, start_index_name)
                    name_value = line[start_index_name:end_index_name]
                    break
    
        # 输出变量值
        if variable_value is None:
            print(f"未找到变量 {variable_name}")
    
    t = eval(variable_value)
    
    list = []
    if t["1"]['channelStatus'] == 'I':
        list.append(1)
    if t["2"]['channelStatus'] == 'I':
        list.append(2)
    if t["3"]['channelStatus'] == 'I':
        list.append(3)
    if t["4"]['channelStatus'] == 'I':
        list.append(4)
    if t["5"]['channelStatus'] == 'I':
        list.append(5)
    if t["6"]['channelStatus'] == 'I':
        list.append(6)
    if t["7"]['channelStatus'] == 'I':
        list.append(7)
    if t["8"]['channelStatus'] == 'I':
        list.append(8)
    if t["9"]['channelStatus'] == 'I':
        list.append(9)
    if t["10"]['channelStatus'] == 'I':
        list.append(10)
    
    empty = ','.join(str(i) for i in list)
    
    command = 'curl -g "http://api.chuckfang.com/xiaopixiao/charge/{0}{1}{2}"'.format(urllib.parse.quote(name_value), empty, urllib.parse.quote('空闲'))
    # command = 'curl -g "http://api.chuckfang.com/xiaopixiao/charge/{0}_is_empty"'.format(urllib.parse.quote(name_value))
    # os.system('curl -g http://api.chuckfang.com/xiaopixiao/charge/')
    os.system(command)

os.system('curl http://wx.99cda.com/cda-wx/chargingBike.do?q=0400000000013703"&"qType=device"&"openId=ozCzC0n8rFOl8oGUbRNI3imeMb-A -o charge.log')
run()
sleep(3)
os.system('curl http://wx.99cda.com/cda-wx/chargingBike.do?q=0400000000013613"&"qType=device"&"openId=ozCzC0n8rFOl8oGUbRNI3imeMb-A -o charge.log')
run()
sleep(3)
os.system('curl http://wx.99cda.com/cda-wx/chargingBike.do?q=0400000000013573"&"qType=device"&"openId=ozCzC0n8rFOl8oGUbRNI3imeMb-A -o charge.log')
run()