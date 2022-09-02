import random



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



def day_trips(day_trip):
    fun=(random.choice(day_trip))
    print (f'The chosen day trip is {fun}')
    confirm = input (f'If you are excited about this activity enter Yes, if you would like to see another enter No')
    if confirm == 'No':
        print (day_trips(day_trip))
    if confirm =='Yes':
        print (f'Your chosen activity is {fun}!')
    return fun



def transports(transport):
    travel=(random.choice(transport))
    print (f'The chosen method of transport is {travel}')
    confirm = input (f'IF you like this method of travel enter Yes, to see another travel option enter No.')
    if confirm == 'No':
        print (transports(transport))
    if confirm == 'Yes':
        print (f'Your chosen method of transport is {travel}!')
    return travel

# def users_answer(answer):
#     user_input=('Please confirm choice.')