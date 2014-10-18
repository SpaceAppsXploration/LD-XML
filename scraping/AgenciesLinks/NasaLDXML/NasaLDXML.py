from bs4 import BeautifulSoup
import json, io, requests, sys, os

lib_path = os.path.abspath("../../")
sys.path.append(lib_path)
from PL_fields import FIELDS

def generate_url(keyword):
    return "http://nasasearch.nasa.gov/search?affiliate=nasa&query=" + keyword.replace(" ", "+") + "&commit=Search"

def retrieve(url):
    print url
    return requests.get(url).text

def parse(html, mission, keyword):
    soup = BeautifulSoup(html)

    keys = ["title", "link", "abstract"]

    data = []

    results = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['searchresult'])

    try:
        for result in results:
            titles = []
            links = []
            abstracts = []

            elements = []
            
            link = result.find("a")
            titles.append(link.text)
            links.append(link['href'])

            i = 0
            for abstract in result.find_all("h3"):
                if i % 2 != 0:
                    abstracts.append(abstract.text)
                i += 1
            #     try:
            #         abstract["class"] 
            #     except KeyError:
            #         abstracts.append(abstract.text)

            for i in range(0, len(titles)):
                    elements.append([titles[i], links[i], abstracts[i]])

            for element in elements:
                data.append(dict(zip(keys, element)))

    except AttributeError:
        print "No results"

    return mission, keyword, data

def save_json(data):
    i = 0
    for row in data:
        i += 1
        with io.open("NasaLDXML.txt", "a", encoding="utf-8") as out_file:
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
i = 0
for mission in missions:
    for field in mission[1]:
        url = generate_url(mission[0] + " " + field)
        html = retrieve(url)
        data.append(parse(html, mission[0], field))

save_json(data)