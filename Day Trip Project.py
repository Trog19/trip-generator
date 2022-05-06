from operator import truediv
import random
from secrets import choice
from tkinter.messagebox import NO, YES


destinations = ['Bozeman', 'Tampa', 'Philadelphia']

# restaurants = ['Rib and Chop', 'Blue Buddah', 'River House']

# day_trip = ['Hiking', 'Fishing', 'Skiing']

# transport = ['Trains', 'Plane', 'Automobile']



def destination(destinations):
    city=(random.choice(destinations))
    return city

Confirm= ['Yes']
user_input= input('Please confirm choice! ')
city= chosen_city=destination(destinations)


chosen_city=destination(destinations)
print (f'The chosen City is {chosen_city}!')
if Confirm == 'No':
    print (chosen_city=destination(destinations))
if Confirm == 'Yes':
    print(f'Your chosen City is {chosen_city}')

# def restaurant(restaurants):
#     dining=(random.choice(restaurants))
#     return dining   

# chosen_restaurant=restaurant(restaurants)
# print (f'Your chosen Restaurant is {chosen_restaurant}!')


# def day_trips(day_trip):
#     fun=(random.choice(day_trip))
#     return fun

# chosen_activity=(random.choice(day_trip))
# print (f'Your day trip activity is {chosen_activity}!') 

# def transports(transport):
#     travel=(random.choice(transport))
#     return travel

# chosen_transport=(random.choice(transport))
# print(f'Your chosen transport is {chosen_transport}!')

# def users_answer(answer):
#     user_input=('Please confirm choice.')