import requests

key = '135b6c4c94b0ecdd0d923483d6831cb5'

city = input('Enter a city: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

data = requests.get(url).json()
degree_sign = u'\N{DEGREE SIGN}'

k = data['main']
for i in k:
    if i[0] == 'f' or i[0] == 't':
        print(f'{i.capitalize()} : {round(k[i]-273, 1)}{degree_sign}C')
    elif i[0] == 'h':
        print(f'{i.capitalize()} : {k[i]}%')
    elif i[0] == 'p':
        print(f'{i.capitalize()} : {k[i]} milibars')
