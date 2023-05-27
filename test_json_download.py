"""
Downloads a json file and saves it

    Parameter: a url pointing to the json file
    
    Returns: saves the file in the current directory

"""

url = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'

# # Writing to sample.json
# import requests
# response = requests.get(url)
# with open("date_details.json", "w") as f:
#     f.write(response.content)


# import pandas as pd
# import requests

# solditems = requests.get(url) # (your url)
# data = solditems.json()
# with open('data.json', 'w') as f:
#     json.dump(data, f)


import requests
import pandas as pd

solditems = requests.get(url) # (your url)
data = solditems.json()

df = pd.DataFrame.from_dict(data)
df.to_csv('date_details.csv')