from googleapiclient.discovery import build
import pprint
import csv



my_api_key = "" #Your API Key
my_cse_id = "" #Your Google Custom Search Engine ID

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    #return res['items']
    return res["searchInformation"]["totalResults"]

with open('Search_terms.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ',')
	headers = next(readCSV,None)
	keywords = []
	for row in readCSV:
		keywords.append(row[0])


print(keywords)
results = []
for keyword in keywords:
	resultsCount = google_search(keyword, my_api_key, my_cse_id)
	#resultsCount = len(keyword)
	results.append({"keyword":keyword, "resultCount": resultsCount})

pprint.pprint(results)

keys = results[0].keys()
with open('output_2.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)

