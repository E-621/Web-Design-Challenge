import pandas as pd
from datetime import datetime

cities_df2 = pd.read_csv('Resources/cities.csv')
country_df = pd.read_csv('Resources/country_abbreviation.csv')

cities_df = pd.merge(cities_df2, country_df, on='Country')
cities_df = cities_df.rename(columns={'City_ID':'City ID', 'Country':'Country Abb', 'Country Name':'Country', 'City':'City', 'Date':'Date', 'Max Temp':'Max Temp', 'Cloudiness':'% Cloudiness', 'Wind Speed': 'Wind Speed (mph)', 'Humidity': '% Humidity', 'Lat':'Lat', 'Lng':'Lng'})
cities_df= cities_df[['City ID', 'Country Abb', 'Country', 'City', 'Date', 'Max Temp', '% Cloudiness', 'Wind Speed (mph)', '% Humidity', 'Lat', 'Lng']]
cities_df.drop(columns=['Country Abb'])
cities_df['Date']=pd.to_datetime(cities_df['Date']).dt.date
cities_df.to_html('cities_data.html', index=False)



table = cities_df.to_html()
print(table)