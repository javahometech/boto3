import json
# Open the file containing json
fileData = open('data.json')

# Convert the file to dictionary object
data = json.load(fileData)

print("Name is ", data['Name'])

print("Locations are")

for location in data['Locations']:
    print(location)
