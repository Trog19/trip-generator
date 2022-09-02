# from importlib.abc import Traversable
# from operator import truediv
import random
# from secrets import choice
# from tkinter.messagebox import NO, YES


destinations = ['Bozeman', 'Tampa', 'Philadelphia']

restaurants = ['Rib and Chop', 'Blue Buddah', 'River House']

day_trip = ['Hiking', 'Fishing', 'Skiing']

transport = ['Train', 'Plane', 'Automobile']


#All answeres are case sensetive, please answer 'Yes' or 'No'

def destination():
    city=(random.choice(destinations))
    print(f'The chosen city is {city}!')
    user_input= input('Please confirm choice! ')
    if user_input== 'No':
        destination()
        return city
    elif user_input== 'Yes':
        return city

return_variable_1=destination() #makes 

def restaurant():
    dining=(random.choice(restaurants))
    print(f'The chosen restaurant is {dining}!')
    user_input=input('Please confirm choice! ')
    if user_input== 'No':
        restaurant()
        return dining
    elif user_input== 'Yes':
        return dining

return_variable_2=restaurant()

def day_trips(): 
    fun=(random.choice(day_trip))
    print (f'The chosen Day Trip is {fun}!')
    user_input= input('Please confirm choice! ')
    if user_input== 'No':
        day_trips()
        return fun
    elif user_input == 'Yes':
        return fun
   

return_variable_3=day_trips()


def transports():
    travel=(random.choice(transport))
    print (f'The chosen transportation is {travel}!')
    user_input= input('Please confirm choice! ')
    if user_input == 'No':
        transports()
        return travel
    elif user_input == 'Yes':
       return travel 
    

return_variable_4=transports()

print(f'Your trip details are complete! You will travel to {return_variable_1}, eat at {return_variable_2}, have fun by {return_variable_3} and get there by {return_variable_4}!')
