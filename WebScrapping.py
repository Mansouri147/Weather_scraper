import pandas as pd
import requests
from bs4 import BeautifulSoup

#Casting From F° to C°
def temp_celcius(fahrenheit):
    fahrenheit = int(fahrenheit[0:2])
    fahrenheit = (fahrenheit - 32) * 5 / 9
    fahrenheit = int(fahrenheit)
    fahrenheit = str(fahrenheit) + '°'
    return fahrenheit


page = requests.get('https://weather.com/weather/today/l/36.72,10.34?par=google&temp=c')
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id='LookingAhead')
items = week.find_all(class_='today-daypart-content')
# print(items[0].find(class_='today-daypart-title').get_text())
# print(items[0].find(class_='today-daypart-wxphrase').get_text())
temp = items[0].find(class_='today-daypart-temp').get_text()


period_names = [item.find(class_='today-daypart-title').get_text() for item in items]
short_descriptions = [item.find(class_='today-daypart-wxphrase').get_text() for item in items]
temperaturesF = [item.find(class_='today-daypart-temp').get_text() for item in items]
# print(period_names)
# print(short_descriptions)
# print(temperaturesF)

# takes out every item in temperaturesF and converts it to celius
temperaturesC=[]
for item in temperaturesF:
    item =temp_celcius(item)
    temperaturesC.append(item)


weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': short_descriptions,
        'temperature': temperaturesC,
    })

print(weather_stuff)
weather_stuff.to_csv('weather.csv')
