import urllib2

def get_all_links(page):
	print "Trying to get all links from page= ", page
	links_list = []
	start_index = 0
	end_index = 0
	while True:
		start_index = page.find('<a href="', start_index)
		if (start_index == -1):
			break
		end_index = page.find('"', start_index + 10)
		link = page[start_index + 9: end_index]
		print "link=", link
		links_list.append(link)
		start_index = end_index + 1
	return links_list

def get_page(url):
	response = urllib2.urlopen(url)
	page_source = response.read()
	return page_source

def union(p, q):
	for e in q:
		if e not in p:
			p.append(e)
	
def crawl_web(seed):
	to_crawl = [seed]
	crawled = []
	while to_crawl:
		url = to_crawl.pop()
		print "Got uncrawled url= ", url
		if url not in crawled:
			crawled.append(url)
			url_page = get_page(url)
			links = get_all_links(url_page)
			union(to_crawl, links)
			print to_crawl
	return crawled

seed = "http://www.udacity.com/cs101x/index.html"
print crawl_web(seed)
	
#page = get_page("http://www.udacity.com/cs101x/index.html")
#page = get_page("http://openology.blogspot.in")
#page = get_page("http://en.wikipedia.org/wiki/The_Magic_Words_are_Squeamish_Ossifrage")
#print page
#links = get_all_links(page)
#print links


#page = """<html>
#		<body>
#		This is a test page for learning to crawl!
#		<p>
#		It is a good idea to
#		<a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a>
#		before you try to
#		<a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
#		<a href="http://www.udacity.com/cs101x/flying.html">fly</a>.
#		</p>
#		</body>
#		</html>"""
#return page