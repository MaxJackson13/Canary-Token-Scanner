from zipfile import ZipFile
import xml.etree.ElementTree as et
import re

zipfile = ZipFile('Downloads/canary.docx')
files = zipfile.namelist()
rels = [rel for rel in files if rel.endswith('.rels')]

pattern = re.compile(r"^https?://canarytokens.com/.*(/contact.php)$")

tokens = []

for rel in rels:
    
    file = zipfile.open(rel, 'r')
    
    tree = et.parse(file)
    root = tree.getroot()
    
    for child in root:
        
        if 'TargetMode' in child.attrib.keys() and child.attrib['TargetMode'] == 'External':
            
            target = child.attrib['Target']
            typ = child.attrib['Type']
            
            if pattern.search(target):
                tokens.append(pattern.search(target).group(0))
            
            print('External link found: ' + target + '\nType: ' + typ.split('/')[-1] + '\n')

print('Possible canary tokens found:\n')
print('\n'.join(tokens))
