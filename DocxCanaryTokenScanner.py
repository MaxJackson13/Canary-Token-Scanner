from zipfile import ZipFile
import xml.etree.ElementTree as et
import re
import argparse
from termcolor import colored

parser = argparse.ArgumentParser()                                                                  
parser.add_argument('-f', '--file', required=True, help = 'path to .docx file')
options = parser.parse_args()

file = options.file

zipfile = ZipFile(file)                                                                             # open the docx file for reading
files = zipfile.namelist()                                                                          # get a list of the files in the docx file
rels = [rel for rel in files if rel.endswith('.rels')]                                              # filter for the *.rels files ]

pattern = re.compile(r"^https?://canarytokens.com/.*(/contact.php)$")                               # regex pattern to match canary token links

tokens = []                                                                                         # create list to hold found canary tokens

for rel in rels:
    
    file = zipfile.open(rel, 'r')                                                                   # read the .rel file
    
    tree = et.parse(file)                                                                           # parse the xml
    root = tree.getroot()                                                                           # get the root element
    
    for child in root:                                                                              # iterate through through child nodes
        
        if 'TargetMode' in child.attrib.keys() and child.attrib['TargetMode'] == 'External':        # find nodes containing external links
            
            target = child.attrib['Target']                                                         # extract the target and type attributes
            typ = child.attrib['Type']
            
            if pattern.search(target):                                                              # check if the target matches for a canary token
                tokens.append(pattern.search(target).group(0))
            
            print('External link found: ' + colored(target,'yellow') + '\nType: ' + typ.split('/')[-1] + '\n')

print(colored('Possible canary tokens found:', 'white', 'on_red') + '\n')
print(colored('\n'.join(tokens), attrs=['bold']))
