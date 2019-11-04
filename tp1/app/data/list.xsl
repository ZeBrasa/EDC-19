<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method = "html" encoding = "utf8" indent = "yes"/>
    <xsl:param name="selection"/>
    <xsl:param name="header"/>
    <xsl:template match="/">
        <h2>
            <xsl:value-of select="$header"/>
        </h2>

        <table border="1">
            <tr bgcolor="#9acd32">
                <th align="left">Name</th>
                <th align="left">ID</th>
                <th align="left">Population</th>
                <th align="left">Total Area</th>
                <th align="left">Population Growth</th>
                <th align="left">Infant Mortality</th>
                <th align="left">GDP Total</th>
                <th align="left">Inflation</th>
                <th align="left">Independence date</th>
            </tr>

            <xsl:for-each select="$selection">
                <tr>
                    <td>
                        <a><xsl:attribute name='href'><xsl:value-of select='@id'/></xsl:attribute>
                            <xsl:value-of select="./name/text()"/>
                        </a>
                    </td>
                    <td><xsl:value-of select="@id"/></td>
                    <td><xsl:value-of select="@population"/></td>
                    <td><xsl:value-of select="@total_area"/></td>
                    <td><xsl:value-of select="@population_growth"/></td>
                    <td><xsl:value-of select="@infant_mortality"/></td>
                    <td><xsl:value-of select="@gdp_total"/></td>
                    <td><xsl:value-of select="@inflation"/></td>
                    <td><xsl:value-of select="@indep_date"/></td>
                </tr>
            </xsl:for-each>
        </table>
    </xsl:template>
</xsl:stylesheet>