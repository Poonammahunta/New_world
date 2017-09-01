import os,sys
import socket
import subprocess
current_path = os.dirname(os.abspath(__file__))
conf_file = current_path+'/../../conf/appviewx.conf'
hostname = socket.gethostname(socket.gethostbyname())
cmd = 'cp '+conf_file+current_path+ '/../../tmp.conf'
subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

class IpTransfer():
    def __init__(self):
        self.conf_data = config_parser(conf-file)



if __name__ == "__main__":
    user_input = sys.argv[1:]
    for ips in user_input:
        if localhost in ips:
            ips.replace(localhost,hostname)
            
