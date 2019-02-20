import urllib.request as urlresponse
import json

opencage_key = 'aa393b66d43b473aa5cc32686cd9f706'
opencage_api = 'https://api.opencagedata.com/geocode/v1/json?key=' + opencage_key

weather_key = 'e27dc67e1e9ed83de174650f3d549bf6'
weather_api = 'https://api.darksky.net/forecast/' + weather_key + '/'


def retrieve_geocode(location):
    encode = location.replace(' ', '+')
    encode = encode.replace(',', '%2C')
    args = '&q=' + encode
    response = urlresponse.urlopen(opencage_api + args)
    data = response.read().decode('utf-8')
    json_object = json.loads(data)
    return json_object['results'][0]['bounds']['northeast']


def retrieve_weather(location):
    geocode = retrieve_geocode(location)
    args = str(geocode['lat']) + ',' + str(geocode['lng']) + '?units=si'
    response = urlresponse.urlopen(weather_api + args)
    data = response.read().decode('utf-8')
    return json.loads(data)
