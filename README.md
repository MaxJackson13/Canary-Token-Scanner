# Canary Tokens

What Are Canary Tokens?
-----------------------
Canary tokens are a tool for threat hunting/ active cyber defense. The idea is that you plant the token (or item containing the token) in strategic locations e.g. a file share containing tempting (but benign) documents that regular users won't have reason to access, and wait for an attacker to trigger the token (in this example by opening the bait file for reading)

One form of canary token is a short script that you can embed in the HTML of a webpage which checks that the domain the site is hosted from matches the legitimate domain who the site belongs to. 

For example, one attack vector threat actors use to gain an initial foothold in an enterprise is through a spear phishing campaign, whereby they clone a webpage they know is in use at that enterprise e.g. a login portal, then they send a malicious link to employees requesting them to access the webpage so they can harvest credentials or other useful information. 

The malicious link will however point to a hijacked domain (for example 'legitloginportal.com' becomes 'legitlogonportal.com'). 

So if the enterprise hosting 'legitloginportal.com' embeds a script checking the domain is actually theirs and not a spoofed one, when the webpage is cloned, the token will remain embedded in HTML and trigger when the page is first accessed, alerting them that there may be a phishing campaign against them.

This script checks webpages for canary tokens before cloning them. It does this by parsing the script tags out of the HTML and checking for certain strings which are always present in the token .
