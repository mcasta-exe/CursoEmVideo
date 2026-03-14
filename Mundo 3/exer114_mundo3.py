import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://mail.google.com/mail/u/0/#inbox')
except:
    print("Site inacessivel")
else:
    print("site acessivel")