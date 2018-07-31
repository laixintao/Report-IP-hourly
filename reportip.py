#!/usr/bin/python
#-*-coding:utf8-*-

__author__ = 'laixintao'

import socket
import fcntl
import time
import struct
import smtplib
import urllib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re
import urllib2

# the e-mail config
# this is just a simple format,this e-mail doesn't exist.
smtpserver = "smtp.sina.com"
username = "reaspberrypi@sina.com"
password = "123456"
sender = "reaspberrypi@sina.com"
receiver = ["receiver@sina.com","master@sina.com"]
subject = "[RPI]IP CHANGED"

# file_path config
file_path = "/root/rootcrons/lastip.txt"

def sendEmail(msghtml):
    msgRoot = MIMEMultipart('related')
    msgRoot["To"] = ','.join(receiver)
    msgRoot["From"] = sender
    msgRoot['Subject'] =  subject
    msgText = MIMEText(msghtml,'html','utf-8')
    msgRoot.attach(msgText)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()


def check_network():
    while True:
        try:
            print "Network is Ready!"
            break
        except Exception , e:
           print e
           print "Network is not ready,Sleep 5s...."
           time.sleep(10)
    return True

def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1",80))
    ipaddr=s.getsockname()[0]
    s.close()
    return ipaddr

class Getmyip:
    def getip(self):
        try:
            myip = self.visit("http://1111.ip138.com/ic.asp")
        except:
            try:
                myip = self.visit("http://ip.chinaz.com/")
            except:
                try:
                    myip = self.visit("http://www.whereismyip.com/")
                    # if you want to add more,use the format "except try"
                    # make sure the most useful link be the first
                except:
                    print "Fail to get the Network ip."
                    print "Get the LAN ip."
                    myip = get_lan_ip()
        return myip
    def visit(self,url):
        opener = urllib2.urlopen(url,timeout=20)
        if url == opener.geturl():
            str = opener.read()
            print "IP information from",url
        return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)

def get_network_ip():
    getmyip = Getmyip()
    localip = getmyip.getip()
    return localip


if __name__ == '__main__':
    check_network()
    ipaddr=get_network_ip()
    lanip=get_lan_ip()
    emailip=str(ipaddr)+" "+str(lanip)
    print(emailip)
    ip_file = open(file_path)
    last_ip = ip_file.read()
    ip_file.close()
    if last_ip == emailip:
        print "IP not change."
    else:
        print "IP changed. New ip: {}".format(emailip)
        ip_file = open(file_path,"w")
        ip_file.write(str(emailip))
        ip_file.close()

        sendEmail(emailip)
        print "Successfully send the e-mail."
