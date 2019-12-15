<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
                xmlns:mon="http://www.semwebtech.org/mondial/10/meta#">

    <xsl:output method = "html" encoding = "utf8" indent = "yes"/>
    <xsl:param name="selection"/>

    <xsl:template match="/">
        <li>
          Name <xsl:value-of select="mon:name"/>
        </li>
  </xsl:template>

</xsl:stylesheet>
