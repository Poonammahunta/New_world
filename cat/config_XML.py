import re

pattern= "PID=0x([\w]+)[\W]+SID=0x([\w]+)"
ex_ecm = ["A1", "A2", "0D", "35"]

init_51 = '''<vbench>
\t<module name="CDL_TransmissionECM_51" cdl_sid="51" j1939_sid= "" enable= "1"  j1939_name="" eddt_version="03" action= "create">
\t<cdl_map param= "CDL_TransmissionECM#1_DeviceID" pid= "80" enable= "1" enable_read= "1" enable_write= "1" value= "510010000400"/>
\t<cdl_map param= "CDL_TransmissionECM#1_EngineSerialNumber" pid= "F810" enable= "0" enable_read= "1" enable_write= "1" value= "3933393939394342"/>
\t<cdl_map param= "CDL_TransmissionECM#1_TransmissionSerialNumber" pid= "F833" enable= "1" enable_read= "1" enable_write= "1" value= "3933393939394342"/>
\t<cdl_map param= "CDL_TransmissionECM#1_ECUSerial_HardwarePartNumber" pid= "F827" enable= "1" enable_read= "1" enable_write= "1" value= "3532433435363737313231313334363638383132"/>
\t<cdl_map param= "CDL_TransmissionECM#1_ECUSoftwarePartNumber" pid= "F814" enable= "1" enable_read= "1" enable_write= "1" value= "31323334353637383149"/>
\t<cdl_map param= "CDL_TransmissionECM#1_ProductID" pid= "F82D" enable= "0" enable_read= "1" value= "5452415330323021"/>\n'''

init_24 ='''<vbench>
\t<module name="CDL_EngineECM_24" cdl_sid="24" j1939_sid= "" enable= "1" j1939_name="0000000000000000" eddt_version="03" action= "create">
\t<cdl_map param= "Engine_24_DeviceID" pid= "80" enable= "1" enable_read= "1" enable_write= "1" value= "240001000100"/>
\t<cdl_map param= "Engine_24_ECUSerialNumber" pid= "F811" enable= "1" enable_read= "1" enable_write= "1" value= "34323334353637373132"/>
\t<cdl_map param= "Engine_24_ECUSerial_HardwarePartNumber" pid= "F827" enable= "1" enable_read= "1" enable_write= "1" value= "3432333435363737313231313334363637393132"/>
\t<cdl_map param= "Engine_24_ECUSoftwarePartNumber" pid= "F814" enable= "1" enable_read= "1" enable_write= "1" value= "31323334353637383149"/>
\t<cdl_map param= "Engine_24_ProductID" pid= "F82D" enable= "0" enable_read= "1" value= "4341543030323021"/>
\t<cdl_map param= "TotalOperatingHours #1" pid= "FC2D" enable= "1" enable_read= "1" enable_write= "1" value= "10"/>
\t<cdl_map param= "Engine_24_EngineSerialNumber" pid= "F810" enable= "1" enable_read= "1" enable_write= "1" value= "3939393939393937"/>
\t<cdl_map param= "Engine_24_TransmissionSerialNumber" pid= "F833" enable= "1" enable_read= "1" enable_write= "1" value= "3939393939393937"/>\n'''

init_74 = '''<vbench>
\t<module name="CDL_Break_74" cdl_sid="74" j1939_sid= "" enable= "1" j1939_name="0000000000000000" eddt_version="03" action= "create">
\t<cdl_map param= "CDL_Integrated_Brake_ControlECM#1_DeviceID" pid= "80" enable= "1" enable_read= "1" enable_write= "1" value= "740010000400"/>
\t<cdl_map param= "CDL_Integrated_Brake_ControlECM#1_ECUSerialNumber" pid= "F811" enable= "1" enable_read= "1" enable_write= "1" value= "35353434353637373134"/>
\t<cdl_map param= "CDL_Integrated_Brake_ControlECM#1_EngineSerialNumber" pid= "F810" enable= "1" enable_read= "1" enable_write= "1" value= "3933393939394344"/>
\t<cdl_map param= "CDL_Integrated_Brake_ControlECM#1_ECUSerial_HardwarePartNumber" pid= "F827" enable= "1" enable_read= "1" enable_write= "1" value= "3532433435363737313231313334363638383134"/>
\t<cdl_map param= "CDL_Integrated_Brake_ControlECM#1_ECUSoftwarePartNumber" pid= "F814" enable= "1" enable_read= "1" enable_write= "1" value= "31323334353637383151"/>
\t<cdl_map param= "CDL_Integrated_Brake_ControlECM#1_ProductID" pid= "F82D" enable= "0" enable_read= "1" value= "5452415330323024"/>\n'''

init_57 = '''<vbench>
\t<module name="CDL_Chassis_57" cdl_sid="57" j1939_sid= "00" enable= "1" j1939_name="0000000000000000" eddt_version="03" action= "create">
\t<cdl_map param= "CDL_ChasisECM#1_DeviceID" pid= "80" enable= "1" enable_read= "1" enable_write= "1" value= "570010000400"/>
\t<cdl_map param= "CDL_ChasisECM#1_ECUSerialNumber" pid= "F811" enable= "1" enable_read= "1" enable_write= "1" value= "35353434353637373133"/>
\t<cdl_map param= "CDL_ChasisECM#1_EngineSerialNumber" pid= "F810" enable= "1" enable_read= "1" enable_write= "1" value= "3933393939394343"/>
\t<cdl_map param= "CDL_ChasisECM#1_ECUSerial_HardwarePartNumber" pid= "F827" enable= "1" enable_read= "1" enable_write= "1" value= "3532433435363737313231313334363638383133"/>
\t<cdl_map param= "CDL_ChasisECM#1_ECUSoftwarePartNumber" pid= "F814" enable= "1" enable_read= "1" enable_write= "1" value= "31323334353637383150"/>
\t<cdl_map param= "CDL_ChasisECM#1_ProductID" pid= "F82D" enable= "0" enable_read= "1" value= "5452415330323020"/>\n'''
init_52 = '''<vbench>
\t<module name="CDL_ImplementECM_52" cdl_sid="52" j1939_sid= "1E" enable= "1"  j1939_name="" eddt_version="03" action= "create">
\t<cdl_map param= "CDL_ImplementECM#1_DeviceID" pid= "80" enable= "1" enable_read= "1" enable_write= "1" value= "520000000103"/>
\t<cdl_map param= "CDL_ImplementECM#1ECUSerialNumber" pid= "F811" enable= "1" enable_read= "1" enable_write= "1" value= "37383934353637373132"/>
\t<cdl_map param= "CDL_ImplementECM#1_EngineSerialNumber" pid= "F810" enable= "1" enable_read= "1" enable_write= "1" value= "3933393939394343"/>
\t<cdl_map param= "CDL_ImplementECM#1ECUSerial_HardwarePartNumber" pid= "F827" enable= "1" enable_read= "1" enable_write= "1" value= "3533333435363737313231313334363632333132"/>
\t<cdl_map param= "CDL_ECUSoftwarePartNumber" pid= "F814" enable= "1" enable_read= "1" enable_write= "1" value= "31323334353637383143"/>
\t<cdl_map param= "CDL_ImplementECM#1ProductID" pid= "F82D" enable= "0" enable_read= "1" value= "494D503030303030"/>\n'''

init_7A = '''<vbench>
\t<module name="CDLStrutECM7A" cdl_sid="7A" j1939_sid= "00" enable= "1" j1939_name="0000000000000000" eddt_version="03" action= "create">
\t<cdl_map param= "CDLstrut_SimECM deviceID" pid= "80" enable= "1" enable_read= "1" enable_write= "1" value= "7A0002000200"/>
\t<cdl_map param= "CDLstrut_SimECM Serailnumber" pid= "F811" enable= "1" enable_read= "1" enable_write= "1" value= "353031354D3535354141"/>\n'''

end_msg = '''\t</module>\n</vbench>'''

def pattern_match(pattern,line):
    match = re.search(pattern,line)
    if match:
        print match.group(1,2)
        return match.group(1,2)
    else:
        return None
    
def get_ecms(filename):
    param_list=[]
    ecm_dict = {}
    with open(filename) as infile:
        for line in infile:
            elem=pattern_match(pattern,line)
            if elem:
                param_list.append(elem)

    for item in param_list:
        if item[1] not in ex_ecm:
            if item[1] in ecm_dict:
                ecm_dict[item[1]].append(item[0])
            else:
                ecm_dict[item[1]] = [item[0]]
                
    return ecm_dict

def get_cdl_map(pid_list):
    wr_msg = ''
    msg1 = "\t<cdl_map param= \""
    for pid in pid_list:
        wr_msg = wr_msg + msg1 + \
                 "PID-" + pid + \
                 "\" pid= \"" +pid.lstrip("0")+ "\" " + \
                 "enable= \"1\" enable_read= \"1\" enable_write= \"1\" value= \"0\"/>\n"
    return wr_msg
       
def createXML(ecm_dict):
    for ecm in ecm_dict.keys():
        wr_msg = get_cdl_map(ecm_dict[ecm])
        with open("CDL_ECM_"+ecm+".xml", "w+") as f1:
            if ecm == '24':
                f1.write(init_24)
            if ecm == '51':
                f1.write(init_51)
            if ecm == '57':
                f1.write(init_57)
            if ecm == '74':
                f1.write(init_74)
            if ecm == '7A':
                f1.write(init_7A)
            f1.write(wr_msg)
            f1.write(end_msg)
    
def main(filename):
    ecm_dict = get_ecms(filename)
    if ecm_dict.keys():
        createXML(ecm_dict)

        
if __name__ == '__main__':
    filename= "793F_2013C_3934695-54_total_mod.txt"
    main(filename)
