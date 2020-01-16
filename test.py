#by Poupae and Uzair

from pprint import pprint
from pandas import pandas

df = pd.DataFrame[
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

# filter whitelist names

millenials = df.query("age < 37")

print(millenials)