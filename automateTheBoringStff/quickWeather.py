#! Python
# quickWeather.py - prints weather for local form CL. 

import json, requests, sys

# Compute local from CL arg.
if len(sys.argv) < 2:
	print('Usage: quickWeather.py locatoin')
	sys.exit()
location = ' '.join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=8a700b35cc3bad564c956d5ff572651b' % (location)
response = requests.get(url)
response.raise_for_status()


# TODO: Load JSON data into  a Python variable.
weatherData = json.loads(response.text)
# print weather des.
w = weatherData['list']
print('Current weather in %s:' %(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tommorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print()
print(w[0])

