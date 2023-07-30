import json

with open("setting.json", 'r') as f:
    setting = json.load(f)

# print(setting, type(setting))

setting["settings"] = tuple(setting["settings"])

print(setting["settings"])

with open("setting_new.json", 'w') as f:
    json.dump(setting, f)

with open("setting_new.json", 'r') as f:
    setting = json.load(f)

print(setting["settings"])

print(repr(json.dumps(setting)))

with open("data.txt", "r") as f:
    data = eval(f.read())

print(data)

fields = ["make", "model", "volume", "power", "year", "id"]
data = [{fields[i]:car[i] for i in range(len(fields))} for car in data]

with open("data.json", 'w') as f:
    json.dump(data, f)