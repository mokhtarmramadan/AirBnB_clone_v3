from models.city import City
from models import storage

states = storage.all('State').values()
print(states)
