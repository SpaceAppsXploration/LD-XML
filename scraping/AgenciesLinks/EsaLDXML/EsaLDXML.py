from bs4 import BeautifulSoup
import json, io, requests, sys, os

lib_path = os.path.abspath("../../")
sys.path.append(lib_path)
from PL_fields import FIELDS

def generate_url(keyword):
    return "http://www.esa.int/esasearch?q=" + keyword.replace(" ", "+")

def retrieve(url):
    print url
    return requests.get(url).text

def parse(html, mission, keyword):
    soup = BeautifulSoup(html)

    keys = ["title", "link", "abstract"]
    titles = []
    links = []
    abstracts = []

    elements = []

    data = []

    results = soup.find("div", class_="sr")

    try:
        for link in results.find_all("a"):
            titles.append(link.text)
            links.append(link["href"])

        for abstract in results.find_all("p"):
            abstracts.append((abstract.text).replace("\n", "").replace("\t", "").strip())

        for i in range(0, len(titles)):
            elements.append([titles[i], links[i], abstracts[i]])

        for element in elements:
            data.append(dict(zip(keys, element)))

    except AttributeError:
        print "No results"

    return mission, keyword, data

def save_json(data):
    for row in data:
        with io.open("EsaLDXML.txt","a", encoding="utf-8") as out_file:
            out_file.write(unicode(json.dumps({"mission": row[0], "keyword": row[1], "urls": row[2]}, ensure_ascii=False, indent=4, separators=(',', ': '))))
    out_file.close()    

missions = []
data = []
#DA TOGLIERE
for field in FIELDS.keys():
    for mission in FIELDS[field]["missions"]:
        if not any(mission in mission_name for mission_name in missions):
            missions.append((mission, [FIELDS[field]["kw"]]))
        else:
            index = [mission_saved[0] for mission_saved in missions].index(mission)
            missions[index][1].append(FIELDS[field]["kw"])

missions.sort()
i = 0
for mission in missions:
    for field in mission[1]:
        i += 1  
        if i < 10:  #DA TOGLIERE
            url = generate_url(mission[0] + " " + field)
            html = retrieve(url)
            data.append(parse(html, mission[0], field))
        else:       #DA TOGLIERE
            break

save_json(data)