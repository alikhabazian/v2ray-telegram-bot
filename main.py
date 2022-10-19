import os
import subprocess
import time
import config
import telegram
from datetime import datetime
from pytz import timezone    

tz = timezone(config.time_zone)
API_TOKEN=config.API_TOKEN
channel_id=config.channel_id
proxy_port=config.proxy_port
bridge_port_input=config.bridge_port_input
message_id=config.message_id
name_server=config.name_server
sleep_time=config.sleep_time
manager_telegram_id=config.manager_telegram_id
limit=config.limit
message=config.message

req=telegram.utils.request.Request(proxy_url=f"socks5h://127.0.0.1:{proxy_port}")
bot=telegram.Bot(API_TOKEN,request =req)


small_command=f"tcp port {bridge_port_input}"
some_command = 'sudo tshark -T fields -e ip.src   -f "'+small_command+'" | head -1000 |sort -u'
while(True):
    try:
        p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
        p_status = p.wait()
        (output, err) = p.communicate()
        output1=output.decode('UTF-8')
        print(output1.splitlines())
        leno=len(output1.splitlines())
        I_time = datetime.now(tz)
        bot.editMessageText(f"{message} \n -----------\n{name_server} server {I_time.strftime('%Y/%m/%d %H:%M')} \nOnline users: {leno}\nServer limit: {limit}",chat_id=channel_id,message_id=message_id,timeout=30)
    except Exception as e:
        bot.send_message(manager_telegram_id,f"error is:\n{str(e)}",timeout=1000)
    time.sleep(sleep_time)
