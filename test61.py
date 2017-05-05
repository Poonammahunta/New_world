import os
import datetime
info = os.stat("my.txt")
uid = info.st_uid
print uid
time = info.st_time
print time


