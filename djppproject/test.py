# This code will be used for web scraping with the help of regular expression to extract the mobile number from
# any website that is given as input

from datetime import date

print(date.today())
""" import re,urllib

try:
    import urllib.request
except:
    pass

websites_split = 'unt'.split()
# Asking user to enter the website from which user wants to extract the phone number from...
# websites_name = str(input("Enter the websites name [For example, msn google yahoo]:")) 
# websites_split = websites_name.split()
# regex expression
pat = re.compile(r'\d{1,3}\-\d{1,3}\-\d{1,4}',re.I|re.M)


for s in websites_split:
    print("Searching: " + s)
    try:
            u=urllib.urlopen("https://" + s + ".edu")
    except:
            u=urllib.request.urlopen("https://" + s + ".edu")
    text=u.read()
    # print(type(text))
    # title = re.findall(r'<title>+.*</title>+',str(text),re.I|re.M)
    phone_number = re.findall(pat,str(text))
    print(phone_number[0]) """