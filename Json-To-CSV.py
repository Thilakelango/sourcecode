import pandas as pd
import json
from pandas.io.json import json_normalize

with open('event-sample.json') as f:
    data = json.load(f)
    print(data)
    df = json_normalize(data) # Normalising nested fieldtype
    print(df)
    df.to_csv('full_output.csv', index=False) # create full csv file
    data_read = pd.read_csv("full_output.csv") # read DataFrame
    for (type), group in data_read.groupby(['Type']):
        group.to_csv(f'{type}.csv', index=False) #create csv based on Event Type

