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
