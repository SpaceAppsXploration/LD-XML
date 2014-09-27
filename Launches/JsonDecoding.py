import json, requests

def get_launches(year):
	input_file = open(str(year), "r")
	lines = input_file.readlines()
	input_file.close()

	launches = []

	for line in lines:
		launches.append(line[28:-1])

	return launches

def get_json(launch):
	request = requests.get("http://dbpedia.org/data/" + launch + ".jsond")
	return json.loads(request.text)

def get_abstract(launch, json):
	abstracts = json["http://dbpedia.org/resource/" + launch]["http://dbpedia.org/ontology/abstract"]

	for abstract in abstracts:
		if abstract["lang"] == "en":
			return abstract["value"]

def get_instruments(launch, json):
	instruments_list = []

	try:
		instruments = json["http://dbpedia.org/resource/" + launch]["http://dbpedia.org/property/instruments"]
	except KeyError:
		instruments = []
		instruments_list = []

	for instrument in instruments:
		if instrument["type"] == "literal":
			try:
				if instrument["lang"] == "en":
					instruments_list.append(instrument["value"])
			except KeyError:
				instruments_list.append(instrument["value"])	
		elif instrument["type"] == "uri":
			instruments_list.append(instrument["value"][28:])	
		else:
			print("ERROR")

	return instruments_list

def create_json(launch, abstract, instruments):

	keys = ["uri", "json-uri", "instrumentation", "abstract"]
	elements = ["http://dbpedia.org/page/" + launch, "http://dbpedia.org/data/" + launch + ".jsond", instruments, abstract]

	return dict(zip(keys, elements))

def save_json(date, objects):
	out_file = open(str(date) + ".json","w")
	out_file.write(json.dumps(objects, ensure_ascii=False, indent=4))
	out_file.close()


for year in range(1957, 2015):
	objects = []

	launches = get_launches(year)

	print(year)

	for launch in launches:
	
		print(launch)
	
		json_file = get_json(launch)
		abstract = get_abstract(launch, json_file)
		instruments = get_instruments(launch, json_file)

		objects.append(create_json(launch, abstract, instruments))

	save_json(year, objects)
