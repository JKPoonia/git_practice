#here we creaates a list called cars including string and numbers
cars=['honda', 5, 'hero', 8, 'tesla', 10]
print(cars)
#appends add only one element at the end of list
adding_elements_at_end=cars.append('bmw')
print(cars)

#clear method to remove all elements from the list
removeall=cars.clear()
print(cars) # prints empty list

nations=['india',3, 'usa',4, 'uk',2, 'russia',7]

print(nations)

capitals=['newdelhi','wdc', 'london', 'mosco']

#adding_elements_at_end=nations.extend(capitals)
print(nations)
' extend method is used to add another list to end of given list here we added capitls at the end of nations.'
print(nations.index('usa'))
addelemnt=nations.insert(4,'apple')
print(nations)
print(nations.index(3))
#3.1
my_friends=['ram', 'SHYAM ', 'MOHAN', 'ronit']
print(my_friends[0],my_friends[1])
print(my_friends[2])

print(f'hello my friend',my_friends[0])
print(f'hello my friend {my_friends[1]}')
print(f'hello my friends {my_friends[2]}')

cars=['totya', 'honda', 'hero', 'kia']
for car in cars:
    print(f'í love to ride by car !',car)
#as we did in past that by printing each line manuelly we automate this by using for loop it save lot of time.

nations=['india',3, 'usa',4, 'uk',2, 'russia',7]
poping=nations.pop(2)
print(f'showing the popend element',poping)
del nations[0]
print(nations)

fruits=['mango', 'apple', 'orange', 'babana']

fruit=fruits.remove('apple')
print(fruits)

numbers=[1,4,77,3,567,6,33,33,990]
for num in numbers.copy():
    if num<90:
        numbers.remove(num)
print(numbers)

numbers=[1,4,77,3,567,6,33,33,990]
for num in numbers:
    if num==33:
        numbers.remove(num)
print(numbers)
#use .copy method to remove all element as per condition otherwise it remove frist occurance.

#3.4
dinner_invitaion=['modi','rahul','biden', 'tulsi', 'rishi']
print(dinner_invitaion[0], f'welcome to the part')
print(f'welcome to the part', dinner_invitaion[1])
#its long way so use for loop

dinner_invitaion=['modi','rahul','biden', 'tulsi', 'rishi']

#working with list
#looping throw entire list
Magicians= ['alice', 'jai', 'kishan', 'carolina']
for magician in Magicians:
    print(magician)
# also keep in mind when writing your own for loop that you can choose any name you want for the tempory varibale  that
# is accosaiteed with each values in the list. however its usefull to choose meaningfull name that represent a single iteam of list
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:
# doing more work within a loop

magicians=['alice', 'jai', 'kishan', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great show ')

magicians=['alice', 'jai', 'kishan', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great show ')
    print(f'i cant wait to see your next show!! ',magician)

# doing something after a for loop

magicians=['rahul','mohit','ronit','jai']
x=1
print('1')
for magician in magicians:


    print(f'good job friend !', magician)
    print(f'we are eager to see your next eposide! ', magician)
    x = x + 1
    print(x)
print('thankyou all of you friends for such a good show')

#4.1
fav_pizza=['magrita', 'corn', 'peporoni']
for pizza in fav_pizza:
    print(pizza)
for pizza in fav_pizza:
    print(f'i like {pizza} pizza')
print(f'i like {pizza}')
print(f'i like chilli flex and cock')
print(f'i really lpve pizza!')

animals=['lion','tiger', 'lipord', 'cat']
for animal in animals:
    print(animal)
    print(f'{animal} live in jungle')
print(f'all these animals are carnivors')

for value in range(1,6):
    print(value)
for value in range(1,7):
    print(value)
number=list(range(1,6))
print(number)

squares=[]
for value in range(1,6):
    square=value**2
    squares.append(square)
print(squares)

squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
squares=[value**2 for value in range(1,33)]
print(squares)

#4.3
for value in range(1, 21):
    print(value)

value=[]
for va in range(1,100):
    value.append(va)
print(value)
#4.6
odd_number=[]
for value in range(1,21):
    if (value%2!=0):
       odd_number.append(value)
print(odd_number)
#4.7]
multiple_of_three=[]
for number in range(1,31):
    if (number%3==0):
        multiple_of_three.append(number)
print(multiple_of_three)
#or
mult_of_3=list(range(3,31,3))
print(mult_of_3)
#or

print(mult_of_3=list(range(3,31,3)))
print(list(range(3,31,3)))
#4-10.
fav_pizza=['magrita', 'corn', 'peporoni','pan', 'mango']
print(f'first 3 items in the list are',fav_pizza[:3])
print(f'three items from the middle of the list are', fav_pizza[1:3])
print(f'last 3 items{fav_pizza [-3:-1]}')
# 4.11
my_pizza = ['magrita', 'peporoni', 'chilli', 'paper']
my_friends_pizza = my_pizza[:]
my_pizza.append('mango pizza')
my_friends_pizza.append('orange pizza')
print(f'my fav pizzas are ')
for mypizza in my_pizza:
    print(f'-{mypizza}')

for myfriens in my_friends_pizza:
    print(f'\n my friends fav pizza is ', myfriens)
# 4-13
basic_food = ('samosa', 'kasori', 'sangri ki sabgi', 'rabri', 'khata or kadi')

for meal in basic_food:
    print(meal)
basic_food = ('samosa', 'kasori', 'pineapple')
for meal in basic_food:
    print(meal)
# chep 5, if statement
cars = ['audi', 'bmw', 'totya', 'mahindra']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

fruit='mango'
if fruit!='banana':
    print('hii')
banneded_users=['andrive', 'carolina','david']
user='marie'
if user not in banneded_users:
    print(f'{user.title()}, you can post you response if you wish')
'andrive' in banneded_users

age1=12
age2=39
age1>=12 and age2==21
cars=['audi','bmw', 'subaru', 'toyota']

for car in cars:
  if car=='audi':
    print('audi is there')
#5.3
aliean_color=['green']
for alieancolor in aliean_color:
    if alieancolor=='green':
        print('player just earned 5 ppints')
for alieancolor in aliean_color:
    if alieancolor=='pink': # program terminate here because condition fullfiled
        print('player just earned 5 ppints')
    else:
        print('you earned 10 points')
aliean_color='green'
if aliean_color=='red':
    print('player earned 5 points')
elif aliean_color =='yellow':
    print('player just earned 10 points')
elif aliean_color=='red':
    print('player just earned 15 points')
#5.6
age=12
if age<2:
    print('person is baby')
elif 2<age<4:
    print('person is toddler')
elif 4<age<13:
    print('person is kid')
elif 12<age<20:
    print('person is teenager')
elif 20<age<65:
    print('person is adult')
elif age>=65:
    print('person is elder')
favriot_fruit=['mango','apple','banana']
for fruit in favriot_fruit:

    if fruit=='apple':
        print(f'i really like {fruit }')
#5-8
usernames=['admin', 'jai', 'kishan', 'prakesh', 'ramesh']
for username in usernames:
    if username=='admin':
        print(f'hello, {username}, would you like to see a status report ')
    elif username!='admin':
        print(f'hello, {username}, thankyou for loging for again')

#####
usernames=['admin', 'jai', 'kishan', 'prakesh', 'ramesh']
userin=input('please enter your name-')
for username in usernames:
    if username=='admin' and userin==username:
        print(f'hello, {username}, would you like to see a status report ')
    elif username!='admin'and userin==username:
        print(f'hello, {username}, thankyou for loging for again')
    else:
        print('sorry we cant move fruther')
        break
#5.9
empytlist=[]
if empytlist:
 for  empl in empytlist:
    if username=='admin':
        print(f'hello, {username}, would you like to see a status report ')
    elif username!='admin':
        print(f'hello, {username}, thankyou for loging for again')
else:
        print('we need users')

old_users=['jk', 'ram','rohit','rakesh', 'rahul', 'POONIA']
new_user=['jk', 'ram', 'poonia', 'sourabh', ]
for olduser in old_users:
    for newuser in new_user:
        if olduser==newuser:
            print('you have to enter new name')
        else:
            print('good to go')
numbers=list(range(1,21))
for num in numbers:
    if num==1:
        print('1st')
    elif num==2:
        print('2nd')
    elif num ==3:
        print('3rd')
    else:
        print(f'{num}',"th")
