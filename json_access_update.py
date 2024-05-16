import json
f=open("default.json","r")
data=json.load(f)

# Add “back” to side supported list in all countries with name starting with A
# For each country

for country in data:
    if country[0]=='a':                   # check if it's starts with letter a
        for document in data[country]:
            data[country] [document] ['supportedSide'].append("back")
print(data["usa"])



# Add a new country “sww” which has same configuration as “alb” and save the json as a new text file

data["sww"]=data["alb"]         # assign alb value to sww
print(data)

newFile=open("lexConfig.txt","w")      # write mode to open and edit file
newFile.write(json.dumps(data, indent=2))   