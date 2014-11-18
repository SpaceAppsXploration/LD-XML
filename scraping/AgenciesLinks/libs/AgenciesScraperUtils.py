from bs4 import BeautifulSoup, NavigableString
from selenium import webdriver
import json, requests, io 

#TODO: convert to Python3

def generate_nasa_url(keyword):
    """
    Generate NASA's search url from a keyword
    :param keyword: the keyword to use in order to create the url
    :type keyword: string
    :return: url generated
    :rtype: string
    """
    return "http://nasasearch.nasa.gov/search?affiliate=nasa&query=" + keyword.replace(" ", "+") + "&commit=Search"

def generate_jaxa_url(keyword):
    """
    Generate JAXA's search url from a keyword
    :param keyword: the keyword to use in order to create the url
    :type keyword: string
    :return: url generated
    :rtype: string
    """
    return "http://global.jaxa.jp/search.html?&q=" + keyword.replace(" ", "+") + "&sa=Search&siteurl=global.jaxa.jp"

def generate_esa_url(keyword):
    """
    Generate ESA's search url from a keyword
    :param keyword: the keyword to use in order to create the url
    :type keyword: string
    :return: url generated
    :rtype: string
    """
    return "http://www.esa.int/esasearch?q=" + keyword.replace(" ", "+")

def retrieve(url):
    """
    Retrieve the HTML page from an url
    :param url: the url to use in order to retrieve a page
    :type url: string
    :return: complete HTML page
    :rtype: string
    """
    print(url)
    return requests.get(url).text

def retrieve_webdriver(url):
    """
    Retrieve the HTML page from an url with webdriver (used for dynamic page)
    :param url: the url to use in order to retrieve a page
    :type url: string
    :return: complete HTML page
    :rtype: string
    """
    print(url)

    driver = webdriver.Firefox()
    driver.get(url)
    page = driver.page_source
    driver.close()

    return page

def parse_nasa_page(html):
    """
    This function parses the NASA's HTML page 
    :param html: the HTML page to parse
    :type html: string
    :return: a list of all objects parsed
    :rtype: list 
    """
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

            for i in range(0, len(titles)):
                    elements.append([titles[i], links[i], abstracts[i]])

            for element in elements:
                data.append(dict(zip(keys, element)))

    except AttributeError:
        print("No results")

    return data

def parse_jaxa_page(html):
    """
    This function parses the JAXA's HTML page 
    :param html: the HTML page to parse
    :type html: string
    :return: a list of all objects parsed
    :rtype: list 
    """
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

    return data

def parse_esa_page(html):
    """
    This function parses the ESA's HTML page 
    :param html: the HTML page to parse
    :type html: string
    :return: a list of all objects parsed
    :rtype: list 
    """
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
        print("No results" + ", exception: " + str(exception))

    return data

def __get_abstracts_between_img(source):
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

def save_json(name_file, keys, data):
    """
    This function saves in a JSON all the data scraped
    :param name_file: the name of the JSON
    :type name_file: string
    :param keys: the keys of JSON 
    :type keys: list
    :param data: the data scraped to use in order to save it in a JSON file
    :type data: list
    :return: none
    :rtype: none
    """
    i = 0
    for row in data:
        i += 1
        with io.open(name_file, "a", encoding="utf-8") as out_file:
            out_file.write(unicode(json.dumps({keys[0]: row[0], keys[1]: row[1], keys[2]: row[2]}, ensure_ascii=False, indent=4, separators=(',', ': '))))
            if i != len(data):
                out_file.write(unicode(", \n"))
    out_file.close()    

if __name__ == "__main__":

    print("This is a useful module, not a stand-alone script")