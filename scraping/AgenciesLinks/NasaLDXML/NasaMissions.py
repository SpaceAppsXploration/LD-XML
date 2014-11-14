from AgenciesScraperUtils import generate_nasa_url, retrieve, parse_nasa_page, save_json
import sys, os

lib_path = os.path.abspath("../../")
sys.path.append(lib_path)
from PL_fields import FIELDS

if __name__ == "__main__":

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
			url = generate_nasa_url(mission[0] + " " + field)
			html = retrieve(url)
			data.append([mission[0], field, parse_nasa_page(html)])

    save_json("NasaMissions.txt", ["mission", "keyword", "urls"], data)