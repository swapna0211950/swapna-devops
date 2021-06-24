import requests
import json

#Function to get the value of a key_path in case of nested dictionary for a metadata

def get_nested(data, key):
    if key and data:
        element = key[0]
        if element:
            value = data.get(element)
            return value if len(key) == 1 else get_nested(value, key[1:])

#forming the the URL that calls the metadata server to fecth teh values. "recursive=true" always fetches the output as json.
METADATA_URL = 'http://metadata.google.internal/computeMetadata/v1/instance/?recursive=true'
METADATA_HEADERS = {'Metadata-Flavor': 'Google'}
choice = raw_input("Select which metadata you want to query")#enter what metadata you want to view
key =raw_input("Enter the key for which values needs to be fetched")#enter the key/keypath you want to query
paths = key.split("/")
r = requests.get(METADATA_URL, headers=METADATA_HEADERS)
l = r.content
obj = json.loads(l)
disk = obj[choice]


#querying the data that is form of list of dict

if type(disk) == list:
    new_dict = {}
    for element in disk:
        for k, v in element.items():
            new_dict[k] = v
    val_para = new_dict[key]
    print(val_para)

#querying the data that is in form of dict of dict

elif type(disk) == dict:
    x = get_nested(disk, paths)
    print(x)

#querying the data that is in form of dict
else:
    print(disk)