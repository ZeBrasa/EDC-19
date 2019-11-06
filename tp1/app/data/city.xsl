<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:exsl="http://exslt.org/common">

    <xsl:key name="countryById" match="country" use="@id"/>
    <xsl:output method = "html" encoding = "utf8" indent = "yes"/>
    <xsl:param name="selection"/>
    <xsl:template match="/">

        <table class="infobox geography vcard" style="width: 384px; font-size: 88%;">
            <tbody>
                <tr style="height: 48px;">
                    <th class="adr" style="text-align: center; font-size: 1.25em; font-weight: bold; padding: 0.25em 0.33em 0.33em; line-height: 1.2em; height: 48px; width: 438px;" colspan="2">
                        <xsl:value-of select="$selection/name"/>
                        <br />
                        <div style="padding-top: 0.25em; font-weight: normal;">
                            <xsl:value-of select="$selection/localname"/>
                        </div>
                    </th>
                </tr>
                <tr>
                    <th scope="row"> Country</th>
                    <xsl:variable name="idref" select="$selection/@country" />
                    <td style="white-space: nowrap;">
                        <xsl:variable name="country" select="key('countryById', $idref)"/>
                        <a><xsl:attribute name='href'><xsl:value-of select='$country/@id'/></xsl:attribute>
                            <xsl:value-of select="$country/name"/>
                        </a>
                        <span> (<xsl:value-of select="$country/localname"/>)</span>
                        <br />
                    </td>
                </tr>
                <tr>
                    <th scope="row">Coordinates</th>
                    <td>
                        <span><xsl:value-of select="$selection/latitude"/>, <xsl:value-of select="$selection/longitude"/></span>
                    </td>
                </tr>
                <tr>
                    <th scope="row"> Elevation</th>
                    <td><xsl:value-of select="$selection/elevation"/> meters</td>
                </tr>
                <tr class="mergedtoprow" style="height: 18px;">
                    <th style="text-align: left; height: 18px; width: 438px;" colspan="2"> Population</th>
                </tr>
                <tr class="mergedrow" style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> 2011 census</div>
                    </th>
                    <td style="height: 18px; width: 10px;"> <xsl:value-of select="$selection/population"/>
                        <sup id="cite_ref-10-1" class="reference"></sup>
                    </td>
                </tr>
            </tbody>
        </table>
    </xsl:template>
</xsl:stylesheet>