import datetime
from datetime import timedelta

l = 3
st = []
t = datetime.datetime.today().date()
for i in range(l):
    ft = t + timedelta(days= i+1)
    
st.append(ft)
print st    
