import xml.etree.ElementTree as ET
import bisect
doc = ET.iterparse("C:\\Users\\pmahunta\\Desktop\\new\\xml\\sample.xml",events =('start','end'))

my_file = []
sup_dic = {}

def sor_list(doc,my_file):
    for event, elem in doc:
        if event == 'end' and elem.tag == 'Sup_ID':
            bisect.insort(my_file,elem.text)
            elem.clear()
    return my_file 

sup_list=      ['Sup_ID',
               'Sup_Descr',
               'Sup_Addr_Line1',
               'Sup_HouseNum',
               'Sup_Addr_Line2',
               'Sup_Post_Code',
               'Sup_PO_Box',
               'Sup_Zip_Post_Code',
               'Sup_City',
               'Sup_Region',
               'Sup_Country_Code',
               'Sup_Phone',
               'Sup_Duns_Code',
               'Sup_Creation_Date',
               'Sup_Owner',
               'Sup_Owner_is_GLB',
               'Sup_Is_Production',
               'Sup_Is_Internal',
               'Sup_Main_Com',
               'Sup_Is_Minority',
               'Sup_Is_Lev1',
               'Sup_Is_Lev2',
               'Sup_Is_Lev3',
               'Sup_Parent_L2',
               'Sup_Parent_L3',
               'Sup_Status']


a = sor_list(doc,my_file)

for item in a:
    print item
    for event ,elem in doc:
        print elem.tag
        if event == 'end' and elem.tag == 'Suppliers':
            if sup_dic[sup_list[0]] == item and sup_dic[sup_list[-1]] == 'O':
                print "yes"
            else:
                elem.clear()
                sup_dic ={}
                continue
        if event == 'end' and elem.tag != "Suppliers":
            if elem.tag in sup_list:
                sup_dic[elem.tag] = elem.text
        print "ho"        
                
            
                
                
                
       
                    
            


    
    

