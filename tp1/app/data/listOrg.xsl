<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method = "html" encoding = "utf8" indent = "yes"/>
    <xsl:param name="selection"/>
    <xsl:param name="header"/>
    <xsl:template match="/">
        <h2>
            <xsl:value-of select="$header"/>
        </h2>

        <table class="infobox geography vcard" style="width: 384px; font-size: 88%;">
            <tbody>
                <tr style="height: 48px">
                    <th class="adr" style="text-align: center; font-size: 1.25em; font-weight: bold; padding: 0.25em 0.33em 0.33em; line-height: 1.2em; height: 48px; width: 438px;" colspan="2">
                        <xsl:value-of select="$selection/name/text()"/>
                        <br />
                        <div style="padding-top: 0.25em; font-weight: normal;">
                            <xsl:value-of select="$selection/localname/text()"/>
                        </div>
                    </th>
                </tr>
                <tr style="height: 18px;">
                    <th style="height: 28px; width: 428px;" scope="row">
                        <div style="font-weight: normal;">
                            <div style="font-weight: normal;">
                                <strong>Members</strong>
                            </div>
                        </div>
                    </th>
                    <td style="height: 28px; width: 10px;">
                        <ul>
                            <xsl:for-each select="$selection/country">
                                <li> <xsl:value-of select="./text()"/></li>
                            </xsl:for-each>
                        </ul>
                    </td>
                </tr>
                <tr style="height: 35px;">
                    <th style="height: 35px; width: 428px;" scope="row">Established</th>
                    <td style="height: 35px; width: 10px;"><xsl:value-of select="$selection/established"/></td>
                </tr>
            </tbody>
        </table>

    </xsl:template>
</xsl:stylesheet>