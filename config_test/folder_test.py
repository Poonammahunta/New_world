import os
import ConfigParser

ini_file = "CalibrationCreator.ini"
 

Config = ConfigParser.ConfigParser()
Config.read(ini_file)

def config_parse():
    for section_name in Config.sections():
        print 'Section: ', section_name
        for name, value in Config.items(section_name):
            print ' %s = %s' %(name,value)
            try:
                if not os.path.exists(value):
                    os.mkdir(value)
                    print "Folder created: ", value
            except:
                if oct(os.stat(value)[ST_MODE]) == "0100444":
                    print "Path doesnot have write access"    
                else:
                    print "Path does not exist"
                


if__name__ == "__main__":
    config_parse()
        

