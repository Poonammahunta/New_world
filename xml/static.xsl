<?xml version='1.0'?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" encoding="utf-8"/>
<xsl:template match="/">

<xsl:for-each select="dataroot/Suppliers">
<xsl:sort select="Sup_ID"/>
<!--<xsl:copy-of select="."/><xsl:text>&#10;</xsl:text>-->
<xsl:if test="Sup_Status = 'O'">
<Suppliers>
    <Sup_ID><xsl:value-of select="Sup_ID"/></Sup_ID>
    <Sup_Descr><xsl:value-of select="Sup_Descr"/></Sup_Descr>
    <Sup_Addr_Line1><xsl:value-of select="Sup_Addr_Line1"/></Sup_Addr_Line1>
    <Sup_HouseNum><xsl:value-of select="Sup_HouseNum"/></Sup_HouseNum>
    <Sup_Addr_Line2><xsl:value-of select="Sup_Addr_Line2"/></Sup_Addr_Line2>
    <Sup_Post_Code><xsl:value-of select="Sup_Post_Code"/></Sup_Post_Code>
    <Sup_PO_Box><xsl:value-of select="Sup_PO_Box"/></Sup_PO_Box>
    <Sup_Zip_Post_Code><xsl:value-of select="Sup_Zip_Post_Code"/></Sup_Zip_Post_Code>
    <Sup_City><xsl:value-of select="Sup_City"/></Sup_City>
    <Sup_Region><xsl:value-of select="Sup_Region"/></Sup_Region>
    <Sup_Country_Code><xsl:value-of select="Sup_Country_Code"/></Sup_Country_Code>
    <Sup_Phone><xsl:value-of select="Sup_Phone"/></Sup_Phone>
    <Sup_Duns_Code><xsl:value-of select="Sup_Duns_Code"/></Sup_Duns_Code>    
    <Sup_Creation_Date><xsl:value-of select="Sup_Creation_Date"/></Sup_Creation_Date>
    <Sup_Owner><xsl:value-of select="Sup_Owner"/></Sup_Owner>
    <Sup_Owner_is_GLB><xsl:value-of select="Sup_Owner_is_GLB"/></Sup_Owner_is_GLB>
    <Sup_Is_Production><xsl:value-of select="Sup_Is_Production"/></Sup_Is_Production>
    <Sup_Is_Internal><xsl:value-of select="Sup_Is_Internal"/></Sup_Is_Internal>
    <Sup_Main_Com><xsl:value-of select="Sup_Main_Com"/></Sup_Main_Com>  
    <Sup_Is_Minority><xsl:value-of select="Sup_Is_Minority"/></Sup_Is_Minority>
    <Sup_Is_Lev1><xsl:value-of select="Sup_Is_Lev1"/></Sup_Is_Lev1>
	<Sup_Is_Lev2><xsl:value-of select="Sup_Is_Lev2"/></Sup_Is_Lev2>
	<Sup_Is_Lev3><xsl:value-of select="Sup_Is_Lev3"/></Sup_Is_Lev3>
	<Sup_Parent_L2><xsl:value-of select="Sup_Parent_L2"/></Sup_Parent_L2>
	<Sup_Parent_L3><xsl:value-of select="Sup_Parent_L3"/></Sup_Parent_L3>        
    <Sup_Status><xsl:value-of select="Sup_Status"/></Sup_Status>
</Suppliers><xsl:text>&#10;</xsl:text>
</xsl:if>
</xsl:for-each>

</xsl:template>
</xsl:stylesheet>
