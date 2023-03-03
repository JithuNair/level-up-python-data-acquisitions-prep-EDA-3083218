from io import BytesIO #solution to pandas not read bytes type data
import pandas as pd #newer pandas doesn't read bytes type data
import requests

link = "https://3083218.youcanlearnit.net/dataTable.html"

response = requests.get("https://3083218.youcanlearnit.net/rank.json?_=1677874197653")

state_data = pd.read_json(BytesIO(response.content))

state_data = pd.DataFrame(state_data['data'].to_list(), columns = ['rank', 'state', 'rainfall'])

print(state_data)