import os
import subprocess
import config
import telegram
API_TOKEN=config.API_TOKEN
user_id=684630739
bot=telegram.Bot(API_TOKEN)
some_command = 'sudo tshark -T fields -e ip.src   -f "tcp port 1310" | head -1000 |sort -u'
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
p_status = p.wait()
(output, err) = p.communicate()
output1=output.decode('UTF-8')
leno=len(output1.split('\\n'))+1
bot.send_message(user_id,f"There are {leno} online:\n {output1}")
