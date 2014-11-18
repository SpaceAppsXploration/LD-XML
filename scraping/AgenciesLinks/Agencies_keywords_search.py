"""
Crawl Search Engines and Return Three JSON files
"""


from libs.keywords import JPL_keywords
import libs.AgenciesScraperUtils as Scraping

if __name__ == "__main__":

    ###
    NASA = []

    for key, value in JPL_keywords.items():
        for keyword in value:
            url = Scraping.generate_nasa_url(keyword)
            html = Scraping.retrieve(url)
            NASA.append([key, keyword, Scraping.parse_nasa_page(html)])

    Scraping.save_json("NasaKeywords.json", ["key", "keyword", "urls"], NASA)

    ###
    ESA = []

    for key, value in JPL_keywords.items():
        for keyword in value:
            url = Scraping.generate_esa_url(keyword)
            html = Scraping.retrieve(url)
            ESA.append([key, keyword, Scraping.parse_esa_page(html)])

    Scraping.save_json("EsaKeywords.json", ["key", "keyword", "urls"], ESA)

    ###
    JAXA = []

    for key, value in JPL_keywords.items():
        for keyword in value:
            url = Scraping.generate_jaxa_url(keyword)
            html = Scraping.retrieve_webdriver(url)
            JAXA.append([key, keyword, Scraping.parse_jaxa_page(html)])

    Scraping.save_json("JaxaKeywords.json", ["key", "keyword", "urls"], JAXA)