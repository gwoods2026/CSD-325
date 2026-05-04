import requests
import json

#connects to the dnd 5e api
response = requests.get("http://dnd5eapi.co/api/conditions")

#formats the data into a more readable state
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#prints formated data
jprint(response.json())
