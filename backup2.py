import os 
import time 

source=['/home/karim/Доп', '/home/karim/документы']

targer_dir=/home/karim/backup

today=target_dir + os.sep + time.strptime('%Y%m%d')

now = time.strptime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Done:', today)

target=today+os.sep+now+'.zip'

zip_command="zip -qr {0} {1}".format(target, ''.join(source))

if os.system(zip_command)==0:
    print('Done in', target)
else
    print('404')