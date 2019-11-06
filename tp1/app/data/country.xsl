<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:exsl="http://exslt.org/common">

    <xsl:key name="cityById" match="city" use="@id"/>
    <xsl:key name="orgById" match="organization" use="@id"/>
    <xsl:output method = "html" encoding = "utf8" indent = "yes"/>
    <xsl:param name="selection"/>
    <xsl:variable name="root" select="/"/>

    <xsl:template match="/">
        <div class="container">
            <div class="row">
                <div class="col-sm">
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
                            <tr style="height: 18px;">
                                <th style="white-space: nowrap;" scope="row"> Capital</th>
                                <xsl:variable name="idref" select="$selection/@capital" />
                                <td>
                                    <xsl:variable name="capital" select="key('cityById', $idref)"/>
                                    <a><xsl:attribute name='href'><xsl:value-of select='$capital/@id'/></xsl:attribute>
                                        <xsl:value-of select="$capital/name"/>
                                    </a>
                                    <span> (<xsl:value-of select="$capital/localname"/>)</span>
                                    <br />
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    <div style="font-weight: normal;">
                                        <div style="font-weight: normal;">
                                            <strong>Languages</strong>
                                        </div>
                                    </div>
                                </th>
                                <td>
                                    <ul>
                                        <xsl:for-each select="$selection/language">
                                            <li> <xsl:value-of select="./text()"/></li>
                                        </xsl:for-each>
                                    </ul>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row"> Ethnic groups</th>
                                <td>
                                    <div class="plainlist">
                                        <ul>
                                            <xsl:for-each select="$selection/ethnicgroup">
                                                <li style="white-space: nowrap;"> <xsl:value-of select="./@percentage"/>% <xsl:value-of select="."/></li>
                                            </xsl:for-each>
                                        </ul>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row"> Religion</th>
                                <td>
                                    <div class="plainlist">
                                        <ul>
                                            <xsl:for-each select="$selection/religion">
                                                <li style="white-space: nowrap;"> <xsl:value-of select="./@percentage"/>% <xsl:value-of select="."/></li>
                                            </xsl:for-each>
                                        </ul>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row"> Independence</th>
                                <td>In  <xsl:value-of select="$selection/indep_date"/> from  <xsl:value-of select="$selection/indep_date/@from"/></td>
                            </tr>
                            <tr>
                                <th scope="row"> Government</th>
                                <td> <xsl:value-of select="$selection/government"/>
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
                            <tr>
                                <th scope="row">Car code</th>
                                <td> <xsl:value-of select="$selection/@id"/></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="col-sm">
                    <div class="plainlist">
                        <h3>Cities:</h3>
                        <ul>
                            <xsl:for-each select="$selection//city">
                                <li style="white-space: nowrap;">
                                    <a><xsl:attribute name='href'><xsl:value-of select='./@id'/></xsl:attribute>
                                        <xsl:value-of select="./name"/>
                                    </a>
                                </li>
                            </xsl:for-each>
                        </ul>
                    </div>
                </div>

                <div class="col-sm">

                    <xsl:variable name="tokens">
                        <xsl:copy>
                            <xsl:call-template name="tokenize">
                                <xsl:with-param name="text" select="$selection/@memberships"/>
                            </xsl:call-template>
                        </xsl:copy>
                    </xsl:variable>
                    <div class="plainlist">
                        <h3>Part of:</h3>
                        <ul>
                            <xsl:for-each select="exsl:node-set($tokens)/newElement">
                                <xsl:variable name="orgId" select="./@ref"/>

                                <xsl:for-each select="$root">
                                    <xsl:variable name="org" select="key('orgById', $orgId)"/>
                                    <li>
                                        <a><xsl:attribute name='href'><xsl:value-of select='$org/@id'/></xsl:attribute>
                                            <xsl:value-of select="$org/abbrev"/>
                                        </a>
                                    </li>
                                </xsl:for-each>
                            </xsl:for-each>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </xsl:template>

    <xsl:template name="tokenize">
        <xsl:param name="text"/>
        <xsl:param name="delimiter" select="' '"/>
        <xsl:variable name="token" select="substring-before(concat($text, $delimiter), $delimiter)" />
        <xsl:if test="$token">
            <newElement ref="{$token}"/>
        </xsl:if>
        <xsl:if test="contains($text, $delimiter)">
            <!-- recursive call -->
            <xsl:call-template name="tokenize">
                <xsl:with-param name="text" select="substring-after($text, $delimiter)"/>
            </xsl:call-template>
        </xsl:if>
    </xsl:template>

</xsl:stylesheet>