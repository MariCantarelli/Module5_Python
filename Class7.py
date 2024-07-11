#Checking items off a list

color_client = input('Color: ')
colors = ['yellow', 'green', 'blue', 'red']

if color_client.lower() in colors:
    print('In stock')
else:
    print('We dont have this color in stock')