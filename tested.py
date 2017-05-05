from os import stat

p = stat("myfile.txt").st_atime
#userinfo = pwd.getpwuid(p)
print p
