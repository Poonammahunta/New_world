import os,time,smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

path_to_watch = "C:\\Users\\pmahunta\\Desktop\\new\\xls"
print "watching: " +path_to_watch
before = dict([(f,None) for f in os.listdir(path_to_watch)])
while True:
    after = dict([(f,None) for f in os.listdir(path_to_watch)])
    added = [i for i in after if i not in before]
    removed = [i for i in before if i not in after]
    if removed:
        print "Removed: "",".join(removed)
