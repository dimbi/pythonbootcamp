import requests
import lxml.html

"""
Big idea - write a generalized wev scraper

web scraper functions:

1 download links
2 download images
3 download files
4 download tables
Big O notation
"""

"""
def get_links(url, base_url): 
	response = requests.get(url)
	html = lxml.html.fromstring(response.text)
	links = html.xpath("//a/@href")
	for ind.val in enumerate(links): #used when the index is implicit
	if not "http" in val:
		links[ind] = base_url + val
	return links
"""

def get_images(url):
	response = requests.get(url)
	html = lxml.html.fromstring(response.text)
	print html
	images = html.xpath("//img/@href")
	for image in images:
		name = image.split("/")[-1]
		with open(name,"wb") as f:
			r = requests.get(image)
			f.write(r.content)
	os.chdir("../")

def get_tables(url):
	response = requests.get(url)
	html = lxml.html.fromstring(response.text)
	print html
	tables = html.xpath("//table")
    for table in tables:
    	head = table.xpath("/thead")
    	if head != []:
    		head_data = head.xpath("//tr//th")
    		c_head_data = [i.text_content() for i in head_data]
    	foot = table.xpath("/tfoot")
    	if foot != []:
    		foot_data = foot.xpath("//tr//td")
    		c_foot_data = [i.text_content() for i in foot_data]
    	body = table.xpath("/tbody")
    	if body != []:
    		body_data = body.xpath("//tr//td")
    		c_body_data = [i.text_content() for i in body_data]

    	with open("table"+str(name)+".csv","w") as f:
    		for i in c_head_data:
    			f.write(i+" ")
    		f.write("\n")
    		for i in c_foot_data:
    			f.write(i+" ")
    		f.write("\n")
    		for i in c_body_data:
    			f.write(i+" ")
    		f.write("\n")
	os.chdir("../")


def main():
	url = 'http://www.google.com'
	#get_images(url)

#new line to check
