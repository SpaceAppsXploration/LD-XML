from AgenciesScraperUtils import generate_jaxa_url, retrieve_webdriver, parse_jaxa_page, save_json
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
            url = generate_jaxa_url(mission[0] + " " + field)
            html = retrieve_webdriver(url)
            data.append([mission[0], field, parse_jaxa_page(html)])

    save_json("JaxaMissions.txt", ["mission", "keyword", "urls"], data)