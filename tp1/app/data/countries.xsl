<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:param name="selection"/>
    <xsl:template match="/">
        <h2>Countries</h2>
        <table border="1">
            <tr bgcolor="#9acd32">
                <th align="left">Name</th>
                <th align="left">ID</th>
            </tr>
            <xsl:for-each select="$selection">
                <xsl:sort select="@name" order="ascending"/>
                <tr>
                    <td><xsl:value-of select="@name"/></td>
                    <td><xsl:value-of select="@id"/></td>
                </tr>
            </xsl:for-each>
        </table>
    </xsl:template>
</xsl:stylesheet>