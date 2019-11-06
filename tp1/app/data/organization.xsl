<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:exsl="http://exslt.org/common">

    <xsl:key name="countryById" match="country" use="@id"/>
    <xsl:output method = "html" encoding = "utf8" indent = "yes"/>
    <xsl:param name="selection"/>
    <xsl:variable name="root" select="/"/>

    <xsl:template match="/">
        <table class="infobox geography vcard" style="width: 384px; font-size: 88%;">
            <tbody>
                <tr style="height: 48px;">
                    <th class="adr" style="text-align: center; font-size: 1.25em; font-weight: bold; padding: 0.25em 0.33em 0.33em; line-height: 1.2em; height: 48px; width: 438px;" colspan="2">
                        <xsl:value-of select="$selection/name"/>
                        <br />
                        <div style="padding-top: 0.25em; font-weight: normal;">
                            <xsl:value-of select="$selection/abbrev"/>
                        </div>
                    </th>
                </tr>
                <tr>
                    <th scope="row"> Established</th>
                    <xsl:variable name="idref" select="$selection/@country" />
                    <td style="white-space: nowrap;">
                        <xsl:value-of select="$selection/established"/>
                    </td>
                </tr>
                <tr class="mergedtoprow" style="height: 18px;">
                    <th style="text-align: left; height: 18px; width: 438px;" colspan="2"> Members</th>
                </tr>
                <tr class="mergedrow">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Members</div>
                    </th>
                    <td>
                        <xsl:variable name="tokens">
                            <xsl:copy>
                                <xsl:call-template name="tokenize">
                                    <xsl:with-param name="text" select="$selection/members[@type='member']/@country"/>
                                </xsl:call-template>
                            </xsl:copy>
                        </xsl:variable>
                        <div class="plainlist">
                            <ul>
                                <xsl:for-each select="exsl:node-set($tokens)/newElement">
                                    <xsl:variable name="countryId" select="./@ref"/>

                                    <xsl:for-each select="$root">
                                        <xsl:variable name="country" select="key('countryById', $countryId)"/>
                                        <li>
                                            <a><xsl:attribute name='href'><xsl:value-of select='$country/@id'/></xsl:attribute>
                                                <xsl:value-of select="$country/name"/>
                                            </a>
                                        </li>
                                    </xsl:for-each>
                                </xsl:for-each>
                            </ul>
                        </div>
                    </td>
                </tr>

                <tr class="mergedrow">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Associate members</div>
                    </th>
                    <td>
                        <xsl:variable name="tokens">
                            <xsl:copy>
                                <xsl:call-template name="tokenize">
                                    <xsl:with-param name="text" select="$selection/members[@type='associate member']/@country"/>
                                </xsl:call-template>
                            </xsl:copy>
                        </xsl:variable>
                        <div class="plainlist">
                            <ul>
                                <xsl:for-each select="exsl:node-set($tokens)/newElement">
                                    <xsl:variable name="countryId" select="./@ref"/>

                                    <xsl:for-each select="$root">
                                        <xsl:variable name="country" select="key('countryById', $countryId)"/>
                                        <li>
                                            <a><xsl:attribute name='href'><xsl:value-of select='$country/@id'/></xsl:attribute>
                                                <xsl:value-of select="$country/name"/>
                                            </a>
                                        </li>
                                    </xsl:for-each>
                                </xsl:for-each>
                            </ul>
                        </div>
                    </td>
                </tr>

                <tr class="mergedrow">
                    <th style="height: 18px; width: 428px;" scope="row">
                        <div style="text-indent: -0.9em; margin-left: 1.2em; font-weight: normal;"> Observers</div>
                    </th>
                    <td>
                        <xsl:variable name="tokens">
                            <xsl:copy>
                                <xsl:call-template name="tokenize">
                                    <xsl:with-param name="text" select="$selection/members[@type='observer']/@country"/>
                                </xsl:call-template>
                            </xsl:copy>
                        </xsl:variable>
                        <div class="plainlist">
                            <ul>
                                <xsl:for-each select="exsl:node-set($tokens)/newElement">
                                    <xsl:variable name="countryId" select="./@ref"/>

                                    <xsl:for-each select="$root">
                                        <xsl:variable name="country" select="key('countryById', $countryId)"/>
                                        <li>
                                            <a><xsl:attribute name='href'><xsl:value-of select='$country/@id'/></xsl:attribute>
                                                <xsl:value-of select="$country/name"/>
                                            </a>
                                        </li>
                                    </xsl:for-each>
                                </xsl:for-each>
                            </ul>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
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