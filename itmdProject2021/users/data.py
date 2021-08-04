import requests
import pandas as pd
import json

# Base url for Chicago Open Data Portal crime API; plus addin of date and location filters
baseurl = "https://data.cityofchicago.org/resource/w98m-zvie.json"

datebetw = "?$where=date between '2010-01-01T12:00:00' and '2021-04-30T23:59:00'"

# syntax for below filter is  'within_box(location_col, NW_lat, NW_long, SE_lat, SE_long)'
# boxurl = 'within_box(location, 41.975121, -87.791649, 41.978260, -87.763931)'
# my location to university of chicago 5801 S Ellis Ave, Chicago, IL 60637
boxurl = 'within_box(location, 41.841540, -87.616440, 41.790051, -87.599808)'

# Create the overall URL to interogate API with our data and location filters
ourl = baseurl + datebetw + ' AND ' + boxurl


text =  requests.get(ourl).json()

# print(text)
# print(type(text))
# create pandas dataframe dictionary container object
df = pd.DataFrame(
    text, columns=['date', 'block', 'primary_type', 'arrest',  'description','domestic'])

