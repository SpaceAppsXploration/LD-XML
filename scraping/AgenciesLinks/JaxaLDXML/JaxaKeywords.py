from AgenciesScraperUtils import generate_jaxa_url, retrieve_webdriver, parse_jaxa_page, save_json	
import sys, os

lib_path = os.path.abspath("../../")
sys.path.append(lib_path)
from keywords import JPL_keywords

if __name__ == "__main__":

	data = []

	i = 0
	for key, value in JPL_keywords.items():
		for keyword in value:
			url = generate_jaxa_url(keyword)
			html = retrieve_webdriver(url)
			data.append([key, keyword, parse_jaxa_page(html)])

	save_json("JaxaKeywords.txt", ["key", "keyword", "urls"], data)