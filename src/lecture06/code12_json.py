import sys
import json
from pprint import pprint


data = {
    'big_number': 2 ** 3141,
    'max_float': sys.float_info.max,
    'a_list': [2, 3, 5, 7],
}
pprint(data)
json_data = json.dumps(data)
print(json_data)

data_out = json.loads(json_data)
pprint(data_out)

assert data == data_out  # json and back, data matches

# more options on dumping
info = {
    'full_name': 'Sherlock Holmes',
    'address': {
        'street': '221B Baker St',
        'zip': 'NW1 6XE',
        'city': 'London',
        'country': 'UK',
    }
}
print(json.dumps(info, indent=2, sort_keys=True))

