#by Poupae and Uzair

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#read in the csv file

import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    rows = [dict(row) for row in rows] # Convert OrderedDict to regular dict


#write the csv file

with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color'])
    
    for veg in vegetables:
    	veg_name = veg["name"]
    	veg_color = veg["color"]
    	row = [veg_name, veg_color]
    	writer.writerow(row)
    