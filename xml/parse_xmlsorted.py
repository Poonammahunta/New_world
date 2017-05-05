# -- coding: utf-8 --
#python code to parse xml data
import xml.etree.ElementTree as ET
import sys
import codecs

def update_out_xml(sup_list, sup_dic):
    wr_msg = '<Suppliers>'
    for item in sup_list:
        if sup_dic[item] == None:
            wr_msg = wr_msg + '<' + item + '/>'
        else:
            #wr_msg = wr_msg + '<' + item + '>' + supplier_dic[item].encode('ascii', 'ignore') + '</' + item + '>'
            wr_msg = wr_msg + '<' + item + '>' + sup_dic[item] + '</' + item + '>'
    wr_msg = wr_msg + '</Suppliers>\n'
    return wr_msg

def sor_list(doc,my_file):
    for event, elem in doc:
        if event == 'end' and elem.tag == 'Sup_ID':
            bisect.insort(my_file,elem.text)
    return my_file            

filename = sys.argv[1]
doc = ET.iterparse(filename,events=('start','end'))
my_file = []
sup_dic={}
f = None
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

a = my_file

try:
    f = codecs.open(sys.argv[2], "w", encoding = "utf-8")
    f.write('<?xml version=\"1.0\" encoding=\"utf-8\"?>\n')

    for id in a:
        for event,elem in doc:
            if event == 'end' and elem.tag == "Suppliers":
                if sup_dic[sup_list[0]] == id and sup_dic[sup_list[-1]] == 'O':
                    f.write(update_out_xml(sup_list, sup_dic))
                else:
                    sup_dic = {}
                    elem.clear()
                
            if event == 'end' and elem.tag != "Suppliers":
                if elem.tag in sup_list:
                    sup_dic[elem.tag] = elem.text
finally:
    if f is not None:
        f.close()
                
            
            
    

