from libs import urlloader
import json
from libs import swapi_client

client = swapi_client.Swapi()
people = client.get_people()

print(people)
