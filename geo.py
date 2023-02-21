from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="geo.py")

# address
# location = geolocator.geocode("981 flower fields lane")
# print(location.address)

try:
    q1 = input('write start point address\n')
    q2 = input('write end point address\n')
    location1 = geolocator.geocode(q1)
    location2 = geolocator.geocode(q2)
    lat1, lon1 = location1.latitude, location1.longitude
    lat2, lon2 = location2.latitude, location2.longitude
except:
    print('there was an error with the information provided... try again')

distance = geodesic((lat1, lon1), (lat2, lon2)).miles
print(f'{distance} miles')

