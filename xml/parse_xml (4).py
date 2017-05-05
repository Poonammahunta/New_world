# -- coding: utf-8 --
#python code to parse xml data
import lxml.etree as ET
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

def sort_SupId(doc):
    sort_id=[]
    item = None
    for event,elem in doc:
        if elem.tag == "Sup_ID" and event == "end":
            item = elem.text
        if elem.tag  == "Sup_Status" and event == "end":
            if elem.text == "O" and item != None:
                bisect.insort(sort_id,item)
                item = None
    return sort_id
        
filename = "sample.xml"
sup_dic={}
f = None
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

doc = ET.iterparse(filename,events=('start','end'))
sort_id= sort_SupId(doc)

try:
    f = codecs.open(my_out.xml, "w", encoding = "utf-8")
    f.write('<?xml version=\"1.0\" encoding=\"utf-8\"?>\n')

    for ids in sort_id:
        #print ids
        context=ET.iterparse(filename,events=('start','end'))
        for event,elem in context:
            if event == 'end' and elem.tag == "Suppliers":
                #print supplier_dic
                if sup_dic[sup_list[0]] == ids:
                    f.write(update_out_xml(sup_list, sup_dic))
                    print ids
                    sup_dic = {}
                    elem.clear()
                    while elem.getprevious() is not None:
                        del elem.getparent()[0]
                    del context
                    break
                else:
                    sup_dir={}
            if event == 'end' and elem.tag != "Suppliers":
                if elem.tag in sup_list:
                    sup_dic[elem.tag] = elem.text
finally:
    if f is not None:
        f.close()
            
            
            
    

