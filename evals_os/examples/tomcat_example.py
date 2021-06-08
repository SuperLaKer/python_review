#!/usr/bin/python
import subprocess
import datetime

res = subprocess.Popen("ps -ef | grep tomcat", stdout=subprocess.PIPE, shell=True)
tomcats = res.stdout.readlines()
counts = len(tomcats)

if counts < 4:
    dt = datetime.datetime.now()
    fp = open("/root/tomcat6.txt", 'a')
    fp.write("tomcat6 stop at %s\n" % dt.strftime('%Y-%m-%d %H:%M:%S'))
    fp.close()
    subprocess.Popen('/opt/tomcat7.0/bin/startup.sh', shell=True)

'''
/etc/crontab

crontab -e:
*/30 * * * * root python /root/autorestart-tomcat.py
'''