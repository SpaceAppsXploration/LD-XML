from AgenciesScraperUtils import generate_esa_url, retrieve, parse_esa_page, save_json	
import sys, os

lib_path = os.path.abspath("../../")
sys.path.append(lib_path)
from keywords import JPL_keywords

if __name__ == "__main__":

	data = []

	i = 0
	for key, value in JPL_keywords.items():
		if i < 10:
			for keyword in value:
				url = generate_esa_url(keyword)
				html = retrieve(url)
				data.append([key, keyword, parse_esa_page(html)])
				i = i + 1
		else:
			break

	save_json("EsaKeywords.txt", ["key", "keyword", "urls"], data)