#by Poupae and Uzair

#Reads superheroes.json (in this folder)
import json

with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

#read in the csv file

import csv

with open('superheros.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	rows = [dict(row) for row in rows] # Convert OrderedDict to regular dict

#write the csv file

with open('superheros.csv', 'w') as f:
	writer = csv.writer(f)
	header = ['name', 'age','secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active']
	writer.writerow(header)
	   
	#define members
	members = superheroes['members']

	#Loop thorough the members of the squad, and append the powers of each to the powers array.
	for x in members:
		hero_name = x['name']
		hero_age = x['age']
		hero_id = x['secretIdentity']
		hero_power = x['powers']
		hero_squad = superheroes['squadName']
		hero_hometown = superheroes['homeTown']
		hero_formed = superheroes['formed']
		hero_base = superheroes['secretBase']
		hero_active = superheroes['active']
		row = [hero_name, hero_age, hero_id, hero_power, hero_squad, hero_hometown, hero_formed, hero_base, hero_active]
		writer.writerow(row)
		

