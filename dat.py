import datetime
import calendar
from datetime import timedelta

target = raw_input("Enter the format %Y,%W: " )
p = datetime.datetime.strptime(target,"%Y,%W")

print p

def dat(p):
    st = calendar.day_name[p.weekday()]
    print st
    if st == "Thursday":
        pd = p- timedelta(days=3)
    if st == "Tuesday":
        pd = p-timedelta(days=1)
    if st == "Wednesday":
        pd = p-timedelta(days=2)
    if st == "Friday":
        pd = p-timedelta(days=4)
    if st == "Saturday":
        pd = p-timedelta(days=5)
    if st == "Sunday":
        pd = p-timedelta(days=6)
    if st == "Monday":
        pd = p    
        


    return pd

print dat(p)
        
