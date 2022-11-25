# In this chap we learn to write functions which are named block of code that are designed to one specific job. when we
# want to perform a particular task that we defined in a function , we call the function responsible for it. if we need
# to perform that same task multiple time we call that function.

def greet_users():
    print('hello')


greet_users()


def greet_user(username):
    print(f"Hello, {username.title()}")


greet_user('jai')
greet_user('JAI KISHAN POONIA')

greet_users()  # here we are calling above function its work without copt paste above code or type again.

# 8.1


def display_message():
    print('In this chapter i will going to learn about functions')


display_message()


def favorite_book(title):
    print(f"One of my favorite book is {title}")


favorite_book('Geeta')


def describe_pet(animal_type, pet_name):
    print(f"I have a { animal_type }")
    print(f"my {animal_type}'s name is {pet_name}")


describe_pet('Dog', 'Tommy')
greet_users()  # Calling again above call for test
display_message()

ef describe_pet (animal_type, pet_name):
    print(f'I have a {animal_type}')
    print(f"My {animal_type} name is {pet_name}")


describe_pet(animal_type='hamester', pet_name='harry')
