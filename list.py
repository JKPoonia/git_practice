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


