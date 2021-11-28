import discord
import json
import requests

key_feature = {
    'temp': 'Temperature (°celsius)',
    'feels_like': 'Feels Like(°celsius)',
    'temp_min': 'Minimum Temperature(°celsius)',
    'temp_max': 'Maximum Temperature(°celsius)',
    'humidity': 'Humidity(%Percentage)'
}

def parse_data(data):
    data = data['main']
    if 'pressure' in data:
        del data['pressure']
    if 'sea_level' in data:
        del data['sea_level']
    if 'grnd_level' in data:
        del data['grnd_level']
    return data

def weather_message(data, location):
    location = location.title()
    # location = location.replace("+", " ")
    message = discord.Embed(
        title=f'{location} weather',
        description=f'Here is the weather data for {location}.',
        colour=discord.Colour.from_rgb(158, 158, 158)
    )
    for key in data:
        message.add_field(
            name=key_feature[key],
            value=str(data[key]),
            inline=False
        )
    return message

def find_(place):
    if len(place) >= 1:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&APPID={"Enter your api key here"}&units=metric'     #enter your api key from open weather map website
        print(url)
        data = json.loads(requests.get(url).content)
        data = parse_data(data)
        return weather_message(data, place)

def error_message(location):
    location = location.title()
    location = location.replace("+", " ")
    return discord.Embed(
        title='Error',
        description=f'there was an error retrieving weather data for {location}.',
        colour=discord.Colour.from_rgb(158, 158, 158)
    )

# 6f68b0d15e2c38208bebf781f75e97e5 =====> api key