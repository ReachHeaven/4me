import os 
import time

source=['/home/karim/Доп', '/home/karim/документы']

targer_dir=/home/karim/backup

target=target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'

zip_command="zip -qr {0} {1}".format(target, ''.join(source))

if os.system(zip_command) == 0:
    print('Done in', target)
else
    print('404')