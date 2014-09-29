from bs4 import BeautifulSoup
from selenium import webdriver
import json, io, sys, os, re

lib_path = os.path.abspath("../../")
sys.path.append(lib_path)
from PL_fields import FIELDS

def generate_url(keyword):
	return "http://global.jaxa.jp/search.html?&q=" + keyword.replace(" ", "+") + "&sa=Search&siteurl=global.jaxa.jp"

def retrieve(url):
	print url
	driver = webdriver.Firefox()
	driver.get(url)
	page = driver.page_source
	driver.close()

	return page

def parse(html, mission, keyword):
	soup = BeautifulSoup(html)

	keys = ["title", "link", "abstract"]
	titles = []
	links = []
	abstracts = []

	elements = []

	data = []

	j = 0
	for link in soup.find_all("a", class_="gs-title"): 
		j += 1
		
		if j % 2 == 0 and link.has_attr("href"):
			titles.append(link.text)
			links.append(link['href'])

	for div in soup.find_all("div", class_="gs-bidi-start-align gs-snippet"):
		abstracts.append(" ".join(div.text.split()))

	for i in range(0, len(titles)):
		elements.append([titles[i], links[i], abstracts[i]])

	for element in elements:
		data.append(dict(zip(keys, element)))

	return mission, keyword, data

def save_json(data):
    i = 0
    for row in data:
        i += 1
        with io.open("JaxaLDXML.txt", "a", encoding="utf-8") as out_file:
            out_file.write(unicode(json.dumps({"mission": row[0], "keyword": row[1], "urls": row[2]}, ensure_ascii=False, indent=4, separators=(',', ': '))))
            if i != len(data):
                out_file.write(unicode(", \n"))
    out_file.close()

missions = []
data = []

for field in FIELDS.keys():
    for mission in FIELDS[field]["missions"]:
        if not any(mission in mission_name for mission_name in missions):
            missions.append((mission, [FIELDS[field]["kw"]]))
        else:
            index = [mission_saved[0] for mission_saved in missions].index(mission)
            missions[index][1].append(FIELDS[field]["kw"])

for mission in missions:
    for field in mission[1]:
        url = generate_url(mission[0] + " " + field)
        html = retrieve(url)
        data.append(parse(html, mission[0], field))

save_json(data)