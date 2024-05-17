'''
# use import json to work on json file.
# open json file with read mode., as we don't want to edit the file.
# json file starts and ends with {}, so it's a file object.
# object - Load the content of the file using load() function. store this in new vatialbe(data)
# The content of the file stored in a new variable as dictionary.
'''
import json
f=open("default.json","r")
data=json.load(f)
#print(data)

#objective: To find the number of countries in the given data-dictionary
    # Countries are the key names in dictionary.
    # Use keys() to view all the keys in data.
    # Use len() to count the keys-countries.
countries=list(data.keys())     # store all keys as list
print(countries)
print("Total number of countries:",len(countries))  

#objective: To find the total number of documents present in the file.
    # document names are the key names inside every countries.
    # Need to count the keys in (data["alb"])
    # repeat this for all countris---for loop

total=0                            # to add the count everytime
for i in data:
    documents=list((data[i]).keys())     # Need the keys alone
    print(i,documents)
    count=(len(documents))          # count number of document
    total=total+count
print("Total number of documents:",total)

# Add “back” to side supported list in all countries with name starting with A
# For each country

for country in data:
    if country[0]=='a':                   # check if it's starts with letter a
        for document in data[country]:
            data[country] [document] ['supportedSide'].append("back")
print(data["usa"])



# Add a new country “sww” which has same configuration as “alb” and save the json as a new text file

data["sww"]=data["alb"]
print(data)

newFile=open("lexConfig.txt","w")
newFile.write(json.dumps(data, indent=2))


print("hello")