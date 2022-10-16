import os
import subprocess
import time
import config
import telegram
from datetime import datetime
from pytz import timezone    

Iran = timezone('Iran')
API_TOKEN=config.API_TOKEN
user_id="@rahbazkoon"
proxy_port=8080
bridge_port_input=1210
message_id=67
name_server="Proxy server"
sleep_time=300 # 5 minutes
manager_telegram_id=68463073939

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
        I_time = datetime.now(Iran)
        bot.editMessageText(f"I am {name_server}\n{I_time.strftime('%Y-%m-%d_%H:%M')} \nThere are {leno} online:\n {output1}",chat_id=user_id,message_id=message_id)
    except Exception as e:
        bot.send_message(manager_telegram_id,f"error is:\n{str(e)}")
    time.sleep(sleep_time)
