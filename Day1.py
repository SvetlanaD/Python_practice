import datetime
import requests

# task 1
print('Задача 1')
username = 'Svetlana Denezhkina'
now = datetime.datetime.now().strftime('%H')
if '00' <= now <= '04':
    print(f"Доброй ночи, {username}")
elif '05' <= now <= '09':
    print(f"Доброе утро, {username}")
elif '10' <= now <= '16':
    print(f"Добрый день, {username}")
elif '17' <= now <= '23':
    print(f"Добрый вечер, {username}")

# task 2
print('\nЗадача 2')
response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
now = response.json()['datetime'][11:13]

if '00' <= now <= '04':
    print(f"Доброй ночи, {username}")
elif '05' <= now <= '09':
    print(f"Доброе утро, {username}")
elif '10' <= now <= '16':
    print(f"Добрый день, {username}")
elif '17' <= now <= '23':
    print(f"Добрый вечер, {username}")
