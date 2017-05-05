from bank import Bank

p = Bank("purnima",100)
m = Bank("meenakshi",500)

q = m.transfer("p",100)
print q
