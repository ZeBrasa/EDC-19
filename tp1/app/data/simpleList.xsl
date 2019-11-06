<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method = "html" encoding = "utf8" indent = "yes"/>
    <xsl:param name="selection"/>
    <xsl:template match="/">
        <table>
            <xsl:for-each select="$selection">
                <xsl:sort data-type="text" order="ascending"/>
                <tr>
                    <td>
                        <a><xsl:attribute name='href'><xsl:value-of select='@id'/></xsl:attribute>
                            <xsl:value-of select="./name/text()"/>
                        </a>
                    </td>
                </tr>
            </xsl:for-each>
        </table>
    </xsl:template>
</xsl:stylesheet>
