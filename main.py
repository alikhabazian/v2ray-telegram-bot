import os
import subprocess
import time
import config
import telegram
API_TOKEN=config.API_TOKEN
user_id="@rahbazkoon"
req=telegram.utils.request.Request(proxy_url="socks5h://127.0.0.1:8080")
bot=telegram.Bot(API_TOKEN,request =req)
#bot.send_message("@rahbazkoon","s")
some_command = 'sudo tshark -T fields -e ip.src   -f "tcp port 1210" | head -1000 |sort -u'
while(True):
    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    p_status = p.wait()
    (output, err) = p.communicate()
    output1=output.decode('UTF-8')
    print(output1.splitlines())
    leno=len(output1.splitlines())
    bot.send_message(user_id,f"There are {leno} online:\n {output1}")
    time.sleep(300)
