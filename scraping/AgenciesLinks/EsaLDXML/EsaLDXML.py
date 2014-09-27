from bs4 import BeautifulSoup
import json, io, requests

def retrieve(url):
    return requests.get(url).text

def parse(html):
    soup = BeautifulSoup(html)

    keys = ["title", "link", "abstract"]
    titles = []
    links = []
    abstracts = []

    elements = []

    dataRows = []

    results = soup.find("div", class_="sr")

    for link in results.find_all("a"):
        titles.append(link.text)
        links.append(link['href'])

    for abstract in results.find_all("p"):
        abstracts.append((abstract.text).replace("\n", "").replace("\t", "").strip())

    for i in range(0, len(titles)):
        elements.append([titles[i], links[i], abstracts[i]])

    for element in elements:
        dataRows.append(dict(zip(keys, element)))

    with io.open(url[31:] + ".txt","w", encoding='utf-8') as out_file:
        out_file.write(unicode(json.dumps(dataRows, ensure_ascii=False, indent=4)))
    out_file.close()


urls = ["http://www.esa.int/esasearch?q=2001+Mars+Odyssey+gamma-rays"]#,
#         "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+gravitational+wave",
#         "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+magnetic+fields",
#         "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+microwaves",
#         "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+particles",
#         "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+radio+waves",
#         "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+ultraviolet",
#         "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+visible+light+optical",
#         "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+x-rays",
#         "http://www.esa.int/esasearch?q=ATHENA+gamma-rays",
#         "http://www.esa.int/esasearch?q=ATHENA+visible+light+optical",
#         "http://www.esa.int/esasearch?q=ATHENA+x-rays",
#         "http://www.esa.int/esasearch?q=Cassini+gamma-rays",
#         "http://www.esa.int/esasearch?q=Cassini+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=Cassini+particles",
#         "http://www.esa.int/esasearch?q=Cassini+plasma",
#         "http://www.esa.int/esasearch?q=Cassini+ultraviolet",
#         "http://www.esa.int/esasearch?q=Cassini+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Chandra+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Chandra+x-rays",
#         "http://www.esa.int/esasearch?q=Deep+Impact+%28EPOXI%29+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=Deep+Impact+%28EPOXI%29+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Euclid+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=Euclid+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Gaia+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=Gaia+radio+waves",
#         "http://www.esa.int/esasearch?q=Gaia+ultraviolet",
#         "http://www.esa.int/esasearch?q=Gaia+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Gaia+x-rays",
#         "http://www.esa.int/esasearch?q=Gpm+microwaves",
#         "http://www.esa.int/esasearch?q=Gpm+radio+waves",
#         "http://www.esa.int/esasearch?q=GRAIL+radio+waves",
#         "http://www.esa.int/esasearch?q=HERSCHEL+gamma-rays",
#         "http://www.esa.int/esasearch?q=HERSCHEL+gravitational+wave",
#         "http://www.esa.int/esasearch?q=HERSCHEL+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=HERSCHEL+magnetic+fields",
#         "http://www.esa.int/esasearch?q=HERSCHEL+microwaves",
#         "http://www.esa.int/esasearch?q=HERSCHEL+particles",
#         "http://www.esa.int/esasearch?q=HERSCHEL+plasma",
#         "http://www.esa.int/esasearch?q=HERSCHEL+radio+waves",
#         "http://www.esa.int/esasearch?q=HERSCHEL+ultraviolet",
#         "http://www.esa.int/esasearch?q=HERSCHEL+visible+light+optical",
#         "http://www.esa.int/esasearch?q=HERSCHEL+x-rays",
#         "http://www.esa.int/esasearch?q=Hubble+Space+Telescope+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=Hubble+Space+Telescope+ultraviolet",
#         "http://www.esa.int/esasearch?q=Hubble+Space+Telescope+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Huygens+particles",
#         "http://www.esa.int/esasearch?q=Huygens+plasma",
#         "http://www.esa.int/esasearch?q=Huygens+ultraviolet",
#         "http://www.esa.int/esasearch?q=Integral+gamma-rays",
#         "http://www.esa.int/esasearch?q=Integral+x-rays",
#         "http://www.esa.int/esasearch?q=JUICE+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=JUICE+magnetic+fields",
#         "http://www.esa.int/esasearch?q=JUICE+microwaves",
#         "http://www.esa.int/esasearch?q=JUICE+particles",
#         "http://www.esa.int/esasearch?q=JUICE+plasma",
#         "http://www.esa.int/esasearch?q=JUICE+radio+waves",
#         "http://www.esa.int/esasearch?q=JUICE+ultraviolet",
#         "http://www.esa.int/esasearch?q=JUICE+visible+light+optical",
#         "http://www.esa.int/esasearch?q=JUICE+x-rays",
#         "http://www.esa.int/esasearch?q=Juno+magnetic+fields",
#         "http://www.esa.int/esasearch?q=Juno+microwaves",
#         "http://www.esa.int/esasearch?q=Juno+ultraviolet",
#         "http://www.esa.int/esasearch?q=Juno+visible+light+optical",
#         "http://www.esa.int/esasearch?q=LISA+gravitational+wave",
#         "http://www.esa.int/esasearch?q=LISA+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=LISA+microwaves",
#         "http://www.esa.int/esasearch?q=LISA+x-rays",
#         "http://www.esa.int/esasearch?q=LOFT+magnetic+fields",
#         "http://www.esa.int/esasearch?q=LOFT+particles",
#         "http://www.esa.int/esasearch?q=LOFT+visible+light+optical",
#         "http://www.esa.int/esasearch?q=LOFT+x-rays",
#         "http://www.esa.int/esasearch?q=Mars+2020+Rover+radio+waves",
#         "http://www.esa.int/esasearch?q=Mars+2020+Rover+ultraviolet",
#         "http://www.esa.int/esasearch?q=Mars+2020+Rover+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Mars+2020+Rover+x-rays",
#         "http://www.esa.int/esasearch?q=Mars+Express+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=Mars+Express+particles",
#         "http://www.esa.int/esasearch?q=Mars+Express+plasma",
#         "http://www.esa.int/esasearch?q=Mars+Express+radio+waves",
#         "http://www.esa.int/esasearch?q=Mars+Express+ultraviolet",
#         "http://www.esa.int/esasearch?q=Mars+Express+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+gamma-rays",
#         "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+magnetic+fields",
#         "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+particles",
#         "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+radio+waves",
#         "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+visible+light+optical",
#         "http://www.esa.int/esasearch?q=MAVEN+particles",
#         "http://www.esa.int/esasearch?q=MAVEN+plasma",
#         "http://www.esa.int/esasearch?q=MAVEN+ultraviolet",
#         "http://www.esa.int/esasearch?q=MESSENGER+gamma-rays",
#         "http://www.esa.int/esasearch?q=MESSENGER+gravitational+wave",
#         "http://www.esa.int/esasearch?q=MESSENGER+magnetic+fields",
#         "http://www.esa.int/esasearch?q=MESSENGER+radio+waves",
#         "http://www.esa.int/esasearch?q=MESSENGER+x-rays",
#         "http://www.esa.int/esasearch?q=Nasa+Fermi+GLAST+gamma-rays",
#         "http://www.esa.int/esasearch?q=New+Horizons+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=New+Horizons+radio+waves",
#         "http://www.esa.int/esasearch?q=New+Horizons+ultraviolet",
#         "http://www.esa.int/esasearch?q=New+Horizons+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Nustar+radio+waves",
#         "http://www.esa.int/esasearch?q=Nustar+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Nustar+x-rays",
#         "http://www.esa.int/esasearch?q=Rosetta+gamma-rays",
#         "http://www.esa.int/esasearch?q=Rosetta+gravitational+wave",
#         "http://www.esa.int/esasearch?q=Rosetta+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=Rosetta+magnetic+fields",
#         "http://www.esa.int/esasearch?q=Rosetta+microwaves",
#         "http://www.esa.int/esasearch?q=Rosetta+particles",
#         "http://www.esa.int/esasearch?q=Rosetta+plasma",
#         "http://www.esa.int/esasearch?q=Rosetta+radio+waves",
#         "http://www.esa.int/esasearch?q=Rosetta+ultraviolet",
#         "http://www.esa.int/esasearch?q=Rosetta+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Rosetta+x-rays",
#         "http://www.esa.int/esasearch?q=Solar-Orbiter+particles",
#         "http://www.esa.int/esasearch?q=Solar-Orbiter+plasma",
#         "http://www.esa.int/esasearch?q=STE-QUEST+microwaves",
#         "http://www.esa.int/esasearch?q=STE-QUEST+radio+waves",
#         "http://www.esa.int/esasearch?q=STE-QUEST+visible+light+optical",
#         "http://www.esa.int/esasearch?q=STEREO+plasma",
#         "http://www.esa.int/esasearch?q=STEREO+radio+waves",
#         "http://www.esa.int/esasearch?q=STEREO+ultraviolet",
#         "http://www.esa.int/esasearch?q=STEREO+visible+light+optical",
#         "http://www.esa.int/esasearch?q=THEMIS+magnetic+fields",
#         "http://www.esa.int/esasearch?q=TRMM+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=TRMM+microwaves",
#         "http://www.esa.int/esasearch?q=TRMM+radio+waves",
#         "http://www.esa.int/esasearch?q=Van_Allen+RBSP+particles",
#         "http://www.esa.int/esasearch?q=Van_Allen+RBSP+plasma",
#         "http://www.esa.int/esasearch?q=Venus+Express+magnetic+fields",
#         "http://www.esa.int/esasearch?q=Venus+Express+plasma",
#         "http://www.esa.int/esasearch?q=Venus+Express+radio+waves",
#         "http://www.esa.int/esasearch?q=Venus+Express+ultraviolet",
#         "http://www.esa.int/esasearch?q=Venus+Express+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Voyager+1+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=Voyager+1+magnetic+fields",
#         "http://www.esa.int/esasearch?q=Voyager+1+particles",
#         "http://www.esa.int/esasearch?q=Voyager+1+plasma",
#         "http://www.esa.int/esasearch?q=Voyager+1+ultraviolet",
#         "http://www.esa.int/esasearch?q=Voyager+1+visible+light+optical",
#         "http://www.esa.int/esasearch?q=Voyager+2+infrared+spectrum",
#         "http://www.esa.int/esasearch?q=Voyager+2+magnetic+fields",
#         "http://www.esa.int/esasearch?q=Voyager+2+particles",
#         "http://www.esa.int/esasearch?q=Voyager+2+plasma",
#         "http://www.esa.int/esasearch?q=Voyager+2+radio+waves",
#         "http://www.esa.int/esasearch?q=Voyager+2+ultraviolet",
#         "http://www.esa.int/esasearch?q=Voyager+2+visible+light+optical",
#         "http://www.esa.int/esasearch?q=WISE+%28NEOWISE%29+visible+light+optical",
#         "http://www.esa.int/esasearch?q=XMM-Newton+gamma-rays",
#         "http://www.esa.int/esasearch?q=XMM-Newton+x-rays"]

for url in urls:
    html = retrieve(url)
    parse(html)