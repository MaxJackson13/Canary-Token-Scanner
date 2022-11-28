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

response = requests.get(url)                                                                                # Retrieve contents from the url
soup = BeautifulSoup(response.text, "html.parser")                                                          # Parse the html so we can extract data by tag
scripts = soup.findAll('script')                                                                            # Retrieve all script tags

matches = ['http://canarytokens.com/', target]                                                              # Strings to match in the canary token
encoded_matches = ['\\x'+"\\x".join([hex(ord(char))[-2:] for char in match]) for match in matches]          # Hex encode the strings to match on 
                                                                                                            # obfuscated javascript
token = False
for i,script in enumerate(scripts):
    if all([x in script.text for x in matches]) or all([x in script.text for x in encoded_matches]):        # Check for both the strings in the same script
        print('Token found: '+ '\n' + scripts[i].text)                                                      # block, separating by encoded and plaintext
        token = True
        break                                                                                               # Break once we've found a token and return it
    else:
        pass

if not token:
    print('Token not found')                                                                                # Tell us if no token found 
