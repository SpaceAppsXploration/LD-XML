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

    results = soup.find_all("div", class_="searchresult")

    for result in results:
        link = result.find("a")
        titles.append(link.text)
        links.append(link['href'])

        for h3 in result.find_all("h3"):
            try:
                h3["class"]
            except KeyError:
                abstracts.append(h3.text)

    for i in range(0, len(titles)):
        elements.append([titles[i], links[i], abstracts[i]])

    for element in elements:
        dataRows.append(dict(zip(keys, element)))

    with io.open(url[55:-14] + ".txt","w", encoding='utf-8') as out_file:
        out_file.write(unicode(json.dumps(dataRows, ensure_ascii=False, indent=4)))
    out_file.close()


urls = ["http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+gravitational+wave&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=ATHENA+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=ATHENA+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=ATHENA+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Chandra+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Chandra+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Deep+Impact+%28EPOXI%29+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Deep+Impact+%28EPOXI%29+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Euclid+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Euclid+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gaia+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gaia+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gaia+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gaia+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gaia+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gpm+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gpm+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=GRAIL+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+gravitational+wave&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Hubble+Space+Telescope+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Hubble+Space+Telescope+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Hubble+Space+Telescope+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Huygens+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Huygens+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Huygens+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Integral+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Integral+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Juno+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Juno+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Juno+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Juno+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LISA+gravitational+wave&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LISA+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LISA+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LISA+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LOFT+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LOFT+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LOFT+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LOFT+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+2020+Rover+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+2020+Rover+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+2020+Rover+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+2020+Rover+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MAVEN+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MAVEN+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MAVEN+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MESSENGER+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MESSENGER+gravitational+wave&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MESSENGER+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MESSENGER+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MESSENGER+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Nasa+Fermi+GLAST+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=New+Horizons+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=New+Horizons+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=New+Horizons+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=New+Horizons+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Nustar+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Nustar+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Nustar+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+gravitational+wave&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Solar-Orbiter+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Solar-Orbiter+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STE-QUEST+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STE-QUEST+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STE-QUEST+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STEREO+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STEREO+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STEREO+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STEREO+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=THEMIS+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=TRMM+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=TRMM+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=TRMM+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Van_Allen+RBSP+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Van_Allen+RBSP+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Venus+Express+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Venus+Express+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Venus+Express+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Venus+Express+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Venus+Express+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=WISE+%28NEOWISE%29+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=XMM-Newton+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=XMM-Newton+x-rays&commit=Search"]

for url in urls:
    html = retrieve(url)
    parse(html)