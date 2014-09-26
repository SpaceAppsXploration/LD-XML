from bs4 import BeautifulSoup
from selenium import webdriver
import json, io

urls = ["http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+gamma-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+gravitational+wave&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+microwaves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=2001+Mars+Odyssey+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=ATHENA+gamma-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=ATHENA+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=ATHENA+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Cassini+gamma-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Cassini+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Cassini+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Cassini+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Cassini+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Cassini+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Chandra+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Chandra+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Deep+Impact+%28EPOXI%29+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Deep+Impact+%28EPOXI%29+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Euclid+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Euclid+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Gaia+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Gaia+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Gaia+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Gaia+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Gaia+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Gpm+microwaves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Gpm+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=GRAIL+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+gamma-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+gravitational+wave&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+microwaves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=HERSCHEL+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Hubble+Space+Telescope+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Hubble+Space+Telescope+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Hubble+Space+Telescope+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Huygens+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Huygens+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Huygens+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Integral+gamma-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Integral+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=JUICE+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=JUICE+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=JUICE+microwaves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=JUICE+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=JUICE+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=JUICE+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=JUICE+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=JUICE+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=JUICE+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Juno+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Juno+microwaves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Juno+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Juno+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=LISA+gravitational+wave&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=LISA+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=LISA+microwaves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=LISA+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=LOFT+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=LOFT+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=LOFT+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=LOFT+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+2020+Rover+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+2020+Rover+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+2020+Rover+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+2020+Rover+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Express+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Express+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Express+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Express+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Express+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Express+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Global+Surveyor+gamma-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Global+Surveyor+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Global+Surveyor+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Global+Surveyor+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Global+Surveyor+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Mars+Global+Surveyor+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=MAVEN+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=MAVEN+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=MAVEN+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=MESSENGER+gamma-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=MESSENGER+gravitational+wave&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=MESSENGER+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=MESSENGER+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=MESSENGER+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Nasa+Fermi+GLAST+gamma-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=New+Horizons+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=New+Horizons+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=New+Horizons+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=New+Horizons+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Nustar+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Nustar+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Nustar+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+gamma-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+gravitational+wave&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+microwaves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Rosetta+x-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Solar-Orbiter+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Solar-Orbiter+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=STE-QUEST+microwaves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=STE-QUEST+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=STE-QUEST+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=STEREO+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=STEREO+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=STEREO+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=STEREO+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=THEMIS+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=TRMM+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=TRMM+microwaves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=TRMM+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Van_Allen+RBSP+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Van_Allen+RBSP+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Venus+Express+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Venus+Express+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Venus+Express+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Venus+Express+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Venus+Express+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+1+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+1+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+1+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+1+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+1+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+1+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+2+infrared+spectrum&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+2+magnetic+fields&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+2+particles&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+2+plasma&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+2+radio+waves&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+2+ultraviolet&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=Voyager+2+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=WISE+%28NEOWISE%29+visible+light+optical&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=XMM-Newton+gamma-rays&sa=Search&siteurl=global.jaxa.jp",
		"http://global.jaxa.jp/search.html?&q=XMM-Newton+x-rays&sa=Search&siteurl=global.jaxa.jp"]


def retrieve(url):
	driver = webdriver.Firefox()
	driver.get(url)
	page = driver.page_source
	driver.close()

	return page

def parse(html):
	soup = BeautifulSoup(html)

	keys = ["title", "link", "abstract"]
	titles = []
	links = []
	abstracts = []

	elements = []

	dataRows = []

	i = 0
	for link in soup.find_all("a", class_="gs-title"): 
		i += 1
		
		if i % 2 == 0 and link.has_attr("href"):
			titles.append(link.text)
			links.append(link['href'])

	for div in soup.find_all("div", class_="gs-bidi-start-align gs-snippet"):
		abstracts.append(" ".join(div.text.split()))

	for i in range(0, len(titles)):
		elements.append([titles[i], links[i], abstracts[i]])

	for element in elements:
		dataRows.append(dict(zip(keys, element)))

	with io.open(url[37:-33] + ".txt","w", encoding='utf-8') as out_file:
		out_file.write(unicode(json.dumps(dataRows, ensure_ascii=False, indent=4)))
	out_file.close()


for url in urls:
	html = retrieve(url)
	parse(html)