# When the canary token is obfuscated, the strings the code matches on either remain in cleartext ascii or are hex-encoded but python is smart enough to   
# match the strings to the hex
import requests 
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help = 'url hosting the cloned site')
parser.add_argument('-t', '--target',required=True, help = 'domain of the cloned site e.g. cloned.com')
options = parser.parse_args()

url = options.url
target = options.target

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
scripts = soup.findAll('script')

matches = ['http://canarytokens.com/', target]

token = False
for i,script in enumerate(scripts):
    if all([x in script.text for x in matches]):
        print('Token found: '+ '\n' + scripts[i].text)
        token = True
        break
    else:
        pass

if not token:
    print('Token not found')
