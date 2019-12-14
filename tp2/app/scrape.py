import os
from tp2.settings import BASE_DIR
from lxml import etree

fname = 'cursos.xml'
pname = os.path.join(BASE_DIR, 'app/data/' + fname)
tree = etree.parse(pname)
root = tree.getroot()
courses = pname.xpath('//curso/nome"]/text()')
print(courses)