import requests
import json
import csv
import settings
from dateutil import parser

def extract_data(API_key,freq='D'):
  '''
  Description:
    This function extracts data from the EIA API daily or monthly based on passed in parameters

  Input:
    - API_key: Type(int) This parameter contains the API key. You can get this by registering on EIA platform
    - freq: Type(str) Daily or Monthly aggregation of data. Pass in either D or M. Defaults to daily data. 
  '''
  if freq == 'D' or freq.upper() == 'D':
    name ='daily'
    freq = freq.upper()
  elif freq == 'M' or freq.upper() == 'M':
    name = 'monthly'
    freq = freq.upper()
  else:
    name = 'daily'
    freq = 'D'

  try:
    URL = 'https://api.eia.gov/series/?api_key={0}&series_id=NG.RNGWHHD.{1}'.format(API_key,freq)
  except:
    return "Invalid API key supplied"

  data = requests.get(URL)
  data = json.loads(data.content)
  
  data = data['series'][0]['data']

  with open('data/{0}_prices_henry_hub.csv'.format(name),'wt') as write_file:
    fieldnames = ['date', 'price']
    writer = csv.DictWriter(write_file, fieldnames=fieldnames)
    writer.writeheader()
    #Parse dates from json
    i = 0
    for i,item in enumerate(data):
      try:
        if freq == 'M':
          date = parser.parse(item[0]+'01')
        else:
          date = parser.parse(item[0])
        
        date = date.strftime('%Y-%m-%d')
        
      except Exception as e:
        print(e)
      price = item[1]
      writer.writerow({'date':date,'price':price})
      i += 1
  
  print('{0} lines processed'.format(i))

  
  message = "Data extraction successful"
  print(message)
  return write_file