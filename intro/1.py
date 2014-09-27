import sys
import lxml
from lxml import html
import requests
import webbrowser
import urllib

r=requests.get("http://www.google.com")
r.read()
#tree = html.fromstring(r.text)

urllib.urlretrieve ("http://www.google.com/index.html", "google.html")

#print r
