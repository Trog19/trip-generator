from operator import truediv
import random
from secrets import choice
from tkinter.messagebox import NO, YES


destinations = ['Bozeman', 'Tampa', 'Philadelphia']

restaurants = ['Rib and Chop', 'Blue Buddah', 'River House']

day_trip = ['Hiking', 'Fishing', 'Skiing']

transport = ['Trains', 'Plane', 'Automobile']



def destination(destinations):
    city=(random.choice(destinations))
    print (f'The chosen City is {city}!')
    confirm = input(f'If you are happy with this choice enter Yes, to see another city enter No')
    if confirm == 'No':
        print (destination(destinations))
    if confirm == 'Yes':
        print(f'Your chosen City is {city}')
    return city


def restaurant(restaurants):
    dining=(random.choice(restaurants))
    print (f'The chosen restaurant is {dining}')
    confirm = input (f'If you are happy with this restaurant enter Yes, to see another option enter No')
    if confirm == 'No':
        print (restaurant(restaurants))
    if confirm == 'Yes':
        print(f'Your restaurant is{dining}')
    return dining   



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