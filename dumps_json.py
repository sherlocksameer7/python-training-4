import json as j
data = {"name": "Sameer", "status": "Singer"}
data_json = j.dumps(data)
# dumps() is used for converting dictionary into json !!!
json_data = j.loads(data_json)
print(json_data)
print(json_data["status"])