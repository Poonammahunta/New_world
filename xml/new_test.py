
# -- coding: utf-8 --
#python code to parse xml data

import lxml.etree as ET
import bisect
import codecs
doc = ET.iterparse("C:\\Users\\pmahunta\\Desktop\\new\\xml\\new-data.xml",events =('start','end'))

my_file = []
sup_dic = {}


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
    item = None
    for event, elem in doc:
        if event == "end" and elem.tag == "sup_ID":
            item = elem.text
        if event == 'end' and elem.tag == 'Sup_Status':
            if "Sup_Status" == "O":
                bisect.insort(my_file,item)
                elem.clear()
                item = None
    return my_file

sup_list=['Sup_ID',
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


my_file = sor_list(doc,my_file)
try:
    f = codecs.open("my_out.xml","w",encoding = "utf-8")
    f.write('<?xml version=\"1.0\" encoding=\"utf-8\"?>\n')
    

    for id in my_file:
        docx = ET.iterparse("C:\\Users\\pmahunta\\Desktop\\new\\xml\\new-data.xml",events =('start','end'))
        for event ,elem in docx:
            if event == "end" and elem.tag == "Suppliers":
                if sup_dic[sup_list[0]] == id:
                    f.write(update_out_xml(sup_list, sup_dic))
                    print id
                    sup_dic = {}
                    elem.clear()
                    break
                else:
                    sup_dic= {}
            if event == 'end' and elem.tag != "Suppliers":
                if elem.tag in sup_list:
                    sup_dic[elem.tag] = elem.text


finally:
    f.close()

