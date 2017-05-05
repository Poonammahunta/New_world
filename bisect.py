import bisect
import random
random.seed(1)

l = []
for i in range(1,15):
    r = random.randint(1,100)
    position = bisect.bisect(1, 4)
    bisect.insort(1,r)
    print '%3d %3d' % (r,position),1
    
