#by Poupae and Uzair 

from datetime import datetime

def convert_date(raw_date):
#take string and turn it into python formate
	python_date = datetime.strptime(raw_date, "%d-%B-%y")

#take the python-format date and turn it into string
	date_str = python_date.strftime("%-m/%-d/%Y") 
	return date_str

birthday = "1-May-12"
formatted_birthday = convert_date(birthday)
print(birthday)
print(formatted_birthday)