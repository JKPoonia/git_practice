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
#Default values
def describe_pet (pet_name, animal_type='dog'):
    print(f'i have a {animal_type} ')
    print(f'my {animal_type} name is {pet_name}')


describe_pet(pet_name='willie')

describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster')
#equivalent functions calls
#those functions who has same output
describe_pet('willie')
describe_pet(pet_name='willie')

#FOR HAMSTER
describe_pet('harry','hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#its doesnt matter which calling style we use, as long as function call produce the output we want, just use style which
# we find easiest t understand.
#8.3
def make_shirt(size, text):
    print(f"the size of shirt-{size}, and printed message on it-{text}")


make_shirt(14,'keep working hard')

#8.4
def make_shirt(size=12, message='I love python'):
    print(f"the size of shirt is{size} and the message printed on it is {message}")

make_shirt()
#8.5
def describe_city(city, country='india'):
    print(f"{city} in the {country}")
describe_city('barmer')
#Here we gone to describe the return function
def get_formated_name(first_name, last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formated_name('jimi', 'hendrix')
print(musician)
