#!/usr/bin/python
import sys, os
#path = raw_input("Enter the path for folder/file to search: ")
#folder_exist = raw_input("Enter the folder name to be searched: ")
#dir_exist = os.path.join(path,folder_exist)

try:
    if not os.path.exists(sys.argv[1]):
        os.mkdir(sys.argv[1])
        print "creating New folder", sys.argv[1]
        
    else:
        print "folder exist"

except:
    if not os.path.exists(sys.argv[1][:-1]):
        print "Parent folder does not exist"
    else:
        perm = os.stat()
    print "Please check the drive/path exist"
    
  
        
