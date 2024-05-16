import json

x = open("default.json", 'r')
y = json.load(x)
z = list(y.keys())
print(z)