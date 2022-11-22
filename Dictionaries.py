#Dictionaries allow us to connect pieces of related information.
#Dictionaries inclosed in {} brackets and each key value are seprated by :
# for accesing values in dictionary we use reperance of that dictionary with its key and we get output of value
alien_0={'color': 'green', 'points':5}

smalldic={'name':'jk'}
print(smalldic)

print(alien_0['color'])
print(alien_0['points'])
my_dict={'name':'jai kishan poonia', 'age':'22', 'village':'barmer raj'}
print(my_dict)
my_dict['myfriend']='omprakesh'
print(my_dict)
my_dict['age']='6676ggh'
print(my_dict)
print(my_dict['name'])
friend=my_dict['myfriend']
print(f'my friend name is {friend}')
alien_0={}
alien_0['marchein']='jadu'
alien_0['planet']='march'
alien_0['planet']='bypalnet'
alien_0['name']='sunsinehalftime'

print(alien_0)
car={'color':'black','tyers':4}
print(f"the color of car now={car['color']} ")
car['color']='white'
print(f"the color of car is changed to ={car['color']}")

alien_0={'x_position ':0, 'y_posiion':25, 'speed':'medium'}
print('original position=0')
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position ']=alien_0['x_position ']+x_increment
print(f"new positon : {alien_0['x_position ']}")


students={'name':'jaikishan', 'age':12}
print(students['name'])
jk=students['name']
print(jk)
friends={'name':'op', 'age':14}
print(friends)
#update friends
friends['name']='kartik'
print(friends)
#adding new key value
friends['addresh of kartik']='jodhpur'
print(friends)
fruits={}
fruits['king of fruits']='mango'
fruits['test of mango']='sweet'
print(fruits)
print(f"this is the ling of fruits= {fruits['king of fruits']}")
#removing ke -value pair from the dict
del fruits['test of mango']
print(fruits)

#Creating dictionary by taking input from users
x=1
while x==1:

    user_input={}
    nam=input('plse enter ur name ')
    name=input('plse enter ur age ')
    a=user_input[nam]=name
    print(user_input)
fruits={'mango':'king fruit', 'banana':'best fruit', 'papya':'sweet fruit'}
print(fruits)
coping=fruits.copy()
print(coping)
clear=fruits.clear()
print(fruits)
laptops=['dell', 'lenovo','microsoft' ]
os=['windows', 'android', 'macos']
#6.1
person1={'name':'jk', 'age': 12, 'add':'barmer'}
print(person1['name'].title())
print(person1['add'].title())
#6.2==6.3
peoples_favno={'om':'one','jk':'two', 'k':'four', 'ahg':'five'}
print(f"{peoples_favno['om']} om fav no")
for name, num in peoples_favno.items():
    print(f'{name.title()} fav number {num.title()}')
favorite_language={
    'jen':'python',
    'sarah': 'c',
    'edward':'ruby',
    'phile':'python'
    }
friends=['phile','sarh']
if name in friends:
       language=favorite_language[name].title()
       print(f"\t {name.title()}, i see you loves {language}")

for language in set(favorite_language.values()):
    print(language.title())
#6.4
glossary={'cpu':'is centerl processing unit', 'radio':'wire less voice transfer', 'tv':'telivion'}

for name in favorite_language.keys():
    print(name.title())
#6.5
rivers= {'Ganga': 'india', 'nile':'egypt', 'ámazon':'brizil'}
for river in rivers.keys():
    for countrie in rivers.values():
        print(f"{river} flows from{countrie}")
        break
for river in rivers.keys():
    print(rivers)
    break
for countrie in rivers.values():
    print(countrie)
for river, countries in rivers.items():
    print(rivers)
    print(countries)
