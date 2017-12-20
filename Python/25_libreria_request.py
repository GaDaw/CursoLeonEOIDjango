import requests
import json

response = requests.get('https://httpbin.org/ip')
ip = response.json()['origin']
print('Tu ip es ', ip)


response2= requests.get('https://swapi.co/api/people/')
people = response2.json()['results']
for person in people:
    print (person['name'])

