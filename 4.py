import sys
import lxml
from lxml import html
import requests
import webbrowser
import urllib

r=requests.get("http://oag.ca.gov/missing/stats")
tree = html.fromstring(r.text)
links = tree.xpath('//a')
linkedList = []

for i in links:
   for j in i.values():
      if ".pdf"  in j:
          linkedList.append(j)

print linkedList

#for indx,val in enumerate(linkList):
#	if not "http" in val:
#		j = "http://oag.ca.gov" + val
#		res = requests.get(j)
#		file_name = val.split("/")[-1]
#		with open(file_name,"wb") as f:
#			#text = res.text.encode("ascii","ignore")
#			f.write(text)




#urllib.urlretrieve ("http://www.google.com/index.html", "google.html")

#print r
