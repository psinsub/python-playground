#by Poupae and Uzair

# Read vegetables.csv into a variable called vegetables.
from pprint import pprint
import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows] # Convert OrderedDict to regular dict


# Loop through vegetables and filter down to only green vegtables using a whitelist.
green_veg = []
whitelist = ['okra', 'arugula','broccoli']
for row in vegetables:
    if row['name'] in whitelist:
        green_veg.append(row)


# Print veggies to the terminal
pprint(green_veg)

# Write the veggies to a json file called greenveggies.json
import json

with open('greenveggies.json', 'w') as f:
    json.dump(green_veg, f, indent=4)

#bonus
#Reads json file 
import json

with open('greenveggies.json', 'r') as f:
	green_vegetables = json.load(f)


#write the csv file

with open('green_vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	header = ['name', 'color']
	writer.writerow(header)
	  

	#Loop thorough each green_vegetables 
	for x in green_vegetables:
		name = x['name']
		color = x['color']
		row = [name, color]
		writer.writerow(row)
		

