import csv
import json
# from datetime import datetime
from pprint import pprint

EINSTEIN_CSV = 'Albert, Einstein, 1879-03-14,1955-04-18,Germany,"for his services to Theoretical physics..."'

EINSTEIN = {
    'birthplace': 'Germany',
    'name': 'Albert',
    'surname': 'Einstein',
    'born': '1879-03-14',
    'category': 'physics',
    'motivation': "for his services to Theoretical physics...",
}

einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
print(einstein_json)
pprint(back_to_dict)

with open('laureates.csv', 'r') as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

with open('laureates.json', 'w') as f:
    json.dump(laureates, f, indent=2)



# for laureate in laureates:
#     if laureate['surname'] == 'Einstein':
#         pprint(laureate)
#         print("==========")
#         year_date = datetime.strptime(laureate['year'], "%Y")
#         born_date = datetime.strptime(laureate['born'], "%Y-%m%-%d")
#         print('age', year_date.year - born_date.year)
#         break
