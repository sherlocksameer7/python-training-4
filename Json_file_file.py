import json as j
data = ' {"name": "Sameer", "status": "Singer"} '

json_data = j.loads(data)  # loads is used for parsing it !!! reads !!! as well.
print(json_data["status"])