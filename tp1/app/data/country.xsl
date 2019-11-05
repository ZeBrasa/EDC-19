<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:key name="cityById" match="city" use="@id"/>
    <xsl:output method = "html" encoding = "utf8" indent = "yes"/>
    <xsl:param name="selection"/>
    <xsl:param name="header"/>
    <xsl:template match="/">

        <table class="infobox geography vcard" style="width: 384px; font-size: 88%;">
            <tbody>
                <tr style="height: 48px;">
                    <th class="adr" style="text-align: center; font-size: 1.25em; font-weight: bold; padding: 0.25em 0.33em 0.33em; line-height: 1.2em; height: 48px; width: 438px;" colspan="2">
                        <xsl:value-of select="$selection/name/text()"/>
                        <br />
                        <div style="padding-top: 0.25em; font-weight: normal;">
                            <xsl:value-of select="$selection/localname/text()"/>
                        </div>
                    </th>
                </tr>
                <tr style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row"> Capital</th>
                    <xsl:variable name="idref" select="$selection/@capital" />
                    <td style="height: 18px; width: 10px;"> <xsl:value-of select="key('cityById', $idref)/name"/>
                        <br />
                        <span style="display: none;"> /
                            <span class="geo">38.767; -9.150</span>
                        </span>
                    </td>
                </tr>
                <tr style="height: 18px;">
                    <th style="height: 28px; width: 428px;" scope="row">
                        <div style="font-weight: normal;">
                            <div style="font-weight: normal;">
                                <strong>Languages</strong>
                            </div>
                        </div>
                    </th>
                    <td style="height: 28px; width: 10px;">
                        <ul>
                            <xsl:for-each select="$selection/language">
                                <li> <xsl:value-of select="./text()"/></li>
                            </xsl:for-each>
                        </ul>
                    </td>
                </tr>
                <tr style="height: 45px;">
                    <th style="height: 45px; width: 428px;" scope="row"> Ethnic groups</th>
                    <td style="height: 45px; width: 10px;">
                        <div class="plainlist">
                            <ul>
                                <xsl:for-each select="$selection/ethnicgroup">
                                    <li style="white-space: nowrap;"> <xsl:value-of select="./@percentage"/>% <xsl:value-of select="."/></li>
                                </xsl:for-each>
                            </ul>
                        </div>
                    </td>
                </tr>
                <tr style="height: 96px;">
                    <th style="height: 96px; width: 428px;" scope="row"> Religion</th>
                    <td style="height: 96px; width: 10px;">
                        <div class="plainlist">
                            <ul>
                                <xsl:for-each select="$selection/religion">
                                    <li style="white-space: nowrap;"> <xsl:value-of select="./@percentage"/>% <xsl:value-of select="."/></li>
                                </xsl:for-each>
                            </ul>
                        </div>
                    </td>
                </tr>
                <tr style="height: 35px;">
                    <th style="height: 35px; width: 428px;" scope="row"> Independence</th>
                    <td style="height: 35px; width: 10px;">In  <xsl:value-of select="$selection/indep_date"/> from  <xsl:value-of select="$selection/indep_date/@from"/></td>
                </tr>
                <tr style="height: 35px;">
                    <th style="height: 35px; width: 428px;" scope="row"> Government</th>
                    <td style="height: 35px; width: 10px;"> <xsl:value-of select="$selection/government"/>
                        <br />
                        <sup id="cite_ref-6" class="reference"></sup>
                    </td>
                </tr>
                <tr style="display: none; height: 10px;">
                    <td style="height: 10px; width: 438px;" colspan="2"></td>
                </tr>
                <tr class="mergedtoprow" style="height: 18px;">
                    <th style="text-align: left; height: 18px; width: 438px;" colspan="2"> Area</th>
                </tr>
                <tr class="mergedrow" style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Total</div>
                    </th>
                    <td style="height: 18px; width: 10px;"> <xsl:value-of select="$selection/@area"/> km
                        <sup>2</sup>
                    </td>
                </tr>
                <tr class="mergedbottomrow" style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Border</div>
                    </th>
                    <td style="height: 18px; width: 10px;"> <xsl:value-of select="$selection/border.length"/></td>
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
                <tr class="mergedrow" style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Growth</div>
                    </th>
                    <td style="height: 18px; width: 10px;"> <xsl:value-of select="$selection/population_growth"/>
                        <br />
                        <sup id="cite_ref-imf2_10-2" class="reference"></sup>
                    </td>
                </tr>
                <tr class="mergedbottomrow" style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Infant Mortality</div>
                    </th>
                    <td style="height: 18px; width: 10px;"> <xsl:value-of select="$selection/infant_mortality"/></td>
                </tr>
                <tr class="mergedtoprow" style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">GDP </th>
                    <td style="height: 18px; width: 10px;"></td>
                </tr>
                <tr class="mergedrow" style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Total</div>
                    </th>
                    <td class="mergedrow" style="height: 18px; width: 10px;"> <xsl:value-of select="$selection/gdp_total"/>
                        <br />
                        <sup id="cite_ref-imf2_11-1" class="reference"></sup>
                    </td>
                </tr>
                <tr class="mergedrow" style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Agriculture</div>
                    </th>
                    <td class="mergedrow" style="height: 18px; width: 10px;"> <xsl:value-of select="$selection/gdp_agri"/>
                        <br />
                        <sup id="cite_ref-imf2_11-2" class="reference"></sup>
                    </td>
                </tr>
                <tr class="mergedrow" style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Industry</div>
                    </th>
                    <td style="height: 18px; width: 10px;"> <xsl:value-of select="$selection/gdp_ind"/>
                        <br />
                        <sup id="cite_ref-imf2_11-3" class="reference"></sup>
                    </td>
                </tr>
                <tr class="mergedrow" style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Services</div>
                    </th>
                    <td class="mergedtoprow" style="height: 18px; width: 10px;"> <xsl:value-of select="$selection/gdp_serv"/>
                        <br />
                        <sup id="cite_ref-imf2_11-4" class="reference"></sup>
                    </td>
                </tr>
                <tr style="height: 18px;">
                    <th style="height: 18px; width: 428px;" scope="row">Car code</th>
                    <td style="height: 18px; width: 10px;"> <xsl:value-of select="$selection/@id"/></td>
                </tr>
            </tbody>
        </table>
    </xsl:template>
</xsl:stylesheet>