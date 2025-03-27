import json 

input_file = 'Python_Basics_Training/5_File_Handling/c/data.json'

with open(input_file, 'r') as file:
    data = json.load(file)

for i in data['list']:
    print(f"Name: {i['name']}")
    print(f"Latitude: {i['coord']['lat']}")
    print(f"Longitude: {i['coord']['lon']}")
    print(f"Temperature: {i['main']['temp']}°C")
    print(f"Pressure: {i['main']['pressure']} hPa")
    print(f"Wind Speed: {i['wind']['speed']} m/s")
    print(f"Weather Description: {i['weather'][0]['description']}")
    print('---')