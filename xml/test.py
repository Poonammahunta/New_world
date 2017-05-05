import xml.etree.ElementTree as ET
import bisect
doc = ET.iterparse("C:\\Users\\pmahunta\\Desktop\\new\\xml\\sample.xml",events =('start','end'))

my_file = []
supplier_dic = {}

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



for event ,elem in doc: 
    if event == 'end' and elem.tag != "Suppliers":
        if elem.tag in supplier_list:
            supplier_dic[elem.tag] = elem.text
    if event == 'end' and elem.tag == 'Suppliers':
        #print supplier_dic
        elem.clear()
    if elem.tag == "Sup_ID" and event == 'end':
        bisect.insort(my_file,elem.text)
        for item in my_file:
            if item == elem.text:
                pass
            pass
        supplier_dic[elem.tag] = elem.text
        print supplier_dic
