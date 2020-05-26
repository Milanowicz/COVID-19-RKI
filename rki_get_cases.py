#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os
import requests
import re

now = datetime.datetime.now()
dir_path = os.path.dirname(os.path.abspath(__file__))
CSVLOC = os.path.join(dir_path, 'csv', 'archive')

# Search for all CSV files to get all dates in a list
dates = []
for item in os.listdir(CSVLOC):
    if os.path.isfile(CSVLOC + '/' + item) and item != 'history.csv':
        dates.append(item.replace('rki_', '').replace('.csv', ''))

# Call to RKI page to get HTML as string back
url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
soupurl = requests.get(url).text
soup = BeautifulSoup(soupurl, 'html.parser')
main = soup.find('div', {'id': 'main'})

# Get RKI update time and format it and set it for csv file later
stand = main.find('p').get_text()
rki_update_time = re.sub(r"Stand: (\d+)\.(\d+)\.(\d+).*um\s(\d+):(\d+).*", r"\3-\2-\1 \4:\5", stand)
rki_update_time = pd.to_datetime(rki_update_time)
rki_update_time = rki_update_time.strftime('%Y-%m-%d_%H_%M')
curr_minute = now.strftime("%Y-%m-%d %H:%M")

# Nothing to do, when data already exists
if rki_update_time in dates:
    print('CSV File from Datetime exits')
    exit(1)

# Get cases table from RKI and parse into a Dataframe
table = main.find('table')
columns = ['Bundesland', 'confirmed', 'confirmed_diff', 'extra', 'extra2', 'deaths']
df = pd.read_html(str(table), thousands='.', decimal=',')[0]

# Format DataFrame
df.columns = columns
df['date'] = pd.to_datetime(curr_minute)
df['confirmed'] = df.confirmed.astype(str).str.replace(r'\.', '').astype(int)
df = df[['Bundesland', 'date', 'confirmed', 'deaths']]

# Set csv filename and write DataFrame into it
csv_file = os.path.join(dir_path, 'csv', 'archive', 'rki_' + rki_update_time + '.csv')
df.to_csv(csv_file)
print('Write data to CSV file ' + str(csv_file))
