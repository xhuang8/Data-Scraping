import csv
import json
import pandas as pd

with open("releases.json","r") as file: 
    x = file.read()

x = json.loads(x)

releases = x['releases']
releases = pd.DataFrame(releases)
releases.to_csv("releases.csv", index = False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)