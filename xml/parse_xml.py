# -- coding: utf-8 --
#python code to parse xml data
import xml.etree.ElementTree as ET
import sys
import codecs
import bisect


def update_out_xml(supplier_list, supplier_dic):
    wr_msg = '<Suppliers>'
    for item in supplier_list:
        if supplier_dic[item] == None:
            wr_msg = wr_msg + '<' + item + '/>'
        else:
            #wr_msg = wr_msg + '<' + item + '>' + supplier_dic[item].encode('ascii', 'ignore') + '</' + item + '>'
            wr_msg = wr_msg + '<' + item + '>' + supplier_dic[item] + '</' + item + '>'
    wr_msg = wr_msg + '</Suppliers>\n'
    return wr_msg
a = []
for event ,elem in ET.iterparse("sample.xml",events=('start','end')):
    if elem.tag == "Sup_ID":
        bisect.insort(a,elem.text)
my_file = a
doc = ET.iterparse("sample.xml",events=('start','end'))
supplier_dic={}
f = None
supplier_list=['Sup_ID',
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

try:
    f = codecs.open("sampleout.xml", "w", encoding = "utf-8")
    f.write('<?xml version=\"1.0\" encoding=\"utf-8\"?>\n')

     
    
    for event,elem in doc:
        if event == 'end' and elem.tag == "Suppliers":
            #print supplier_dic
            for item in my_file:
                 supplier_dic[supplier_list[-1]] == "O":
                    f.write(update_out_xml(supplier_list, supplier_dic))
                supplier_dic = {}
                elem.clear()
            
        if event == 'end' and elem.tag != "Suppliers":
            if elem.tag in supplier_list:
                supplier_dic[elem.tag] = elem.text

     
finally:
    if f is not None:
        f.close()
            
            
            
    

