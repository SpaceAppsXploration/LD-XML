from bs4 import BeautifulSoup, NavigableString
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
            link.extract()

        count = 0
        for abstract in results.find_all("p"):
            if len((abstract.text).replace("\n", "").replace("\t", "").strip()) == 0:
                for abastract_between_img in get_abstracts_between_img(results):
                    abstracts.append(abastract_between_img)
            else:    
                abstracts.insert(count - 3, ((abstract.text).replace("\n", "").replace("\t", "").strip()))

            count += 1
        
        for i in range(0, len(titles)):
            elements.append([titles[i], links[i], abstracts[i]])

        for element in elements:
            data.append(dict(zip(keys, element)))

    except AttributeError as exception:
        print "No results" + ", exception: " + str(exception)

    return mission, keyword, data

def get_abstracts_between_img(source):
    abstracts = []
    starts = []

    pieces = source.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['img'])
        
    for piece in pieces:
        start = piece.nextSibling
        starts.append(start)

    i = 1
    for piece in pieces:
        abstract = []
        if i < len(starts):
            while (piece.nextSibling) != starts[i]:
                text = unicode(((piece.nextSibling).string)).replace("\n", "").replace("\t", "").replace("  ", " ").strip()
                if text != "None":
                    abstract.append(text)
                piece = piece.nextSibling
            i += 1
        abstracts.append(" ".join(abstract).strip())

    return abstracts

def save_json(data):
    i = 0
    for row in data:
        i += 1
        with io.open("EsaLDXML.txt", "a", encoding="utf-8") as out_file:
            out_file.write(unicode(json.dumps({"mission": row[0], "keyword": row[1], "urls": row[2]}, ensure_ascii=False, indent=4, separators=(',', ': '))))
            if i != len(data):
                out_file.write(unicode(", \n"))
    out_file.close()    

missions = []
data = [] 

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