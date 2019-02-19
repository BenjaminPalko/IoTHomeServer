import urllib.request as urlresponse
import json
import scripts.country_code_dict as country_code_dict

opencage_key = 'aa393b66d43b473aa5cc32686cd9f706'
opencage_api = 'https://api.opencagedata.com/geocode/v1/json?key=' + opencage_key

cities = {"New York": {40.7128, -74.0060}}
weather_key = 'e27dc67e1e9ed83de174650f3d549bf6'
weather_api = 'https://api.darksky.net/forecast/' + weather_key + '/'


def retrieve_geocode(location):
    # country_code = country_code_dict.COUNTRY_TO_CODE[city.upper()]
    encode = location.replace(' ', '+')
    encode = encode.replace(',', '%2C')
    args = '&q=' + encode
    response = urlresponse.urlopen(opencage_api + args)
    data = response.read().decode('utf-8')
    json_object = json.loads(data)
    return json_object['results'][0]['bounds']['northeast']


def retrieve_weather(latitude, longitude):
    args = str(latitude) + ',' + str(longitude) + '?units=si'
    response = urlresponse.urlopen(weather_api + args)
    data = response.read().decode('utf-8')
    return json.loads(data)


def retrieve_weather(city):
    geocode = retrieve_geocode(city)
    args = str(geocode['lat']) + ',' + str(geocode['lng']) + '?units=si'
    response = urlresponse.urlopen(weather_api + args)
    data = response.read().decode('utf-8')
    return json.loads(data)


def retrieve_weather_by_city(city):
    return retrieve_weather(cities[city][0], cities[city][1])


print(retrieve_weather("Brockville, Ontario")['currently'])
