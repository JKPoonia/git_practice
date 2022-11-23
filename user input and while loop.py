prompt='Tell me numbr'
active=True
while active:
    message= float(input(prompt))
    if message==21:
        active=False
    if message==22:
        active=False
        break
    elif message%2==0:
        print('even')
    elif message%2!=0:
        print('odd')
    else:
        print(message)

y =int(input('enter no'))
x=1
while x<12:
    x=x+1
    if x%2==0:
        continue
    print(x)
#7.1
userinput=input('plese enter the fav car ')
print(f"let me see if i acn find a {userinput} car")
#7.2
userip=input('plse tell, how many people are there in there dinner group')
if int(userip)>=8:
    print('you have to wait')
else:
    print('ur table is ready')
usrip=float(input('plse tell me number i will say wheather its divisible by 10:- '))
if int(usrip)%10==0:
    print('yes number is multiple of 10')
else:
    print('not a multiple of 10')
#7.4 we added some changes as we like in que for random experiment with code
toppings=[]
Active =True
while Active:


    letx=input('please enter ur pizza toppings and if u want to quit plse type-q ')

    if letx=='q':
        Active=False
    else:
        print('ur topping is adding')
    toppings.append(letx)
print(f"we are adding the toping to the pizza ")
for topp in toppings:
    if topp=='q':
        toppings.remove('q')

    else:
           print(topp)
#7.5
ticket=int(input('plse enter ur age'))
active=True
while active:
    if ticket<=3:
        print('ur ticket price is free or no fee')
    elif 3<ticket<=12:
        print('ur ticket price is $10 ')
    else:
        print('ticket price is $12')
    break
#7.8
sandwish_orders=['veg', 'banana', 'green','green']
finished_sandwish=[]
while sandwish_orders:

   for sandwish in sandwish_orders:
    print(f"i made your {sandwish} sandwishes")

    xyz=sandwish_orders.pop()
    finished_sandwish.append(xyz)

print(f"your sandwish are {finished_sandwish}")
print(set(finished_sandwish))

#7.9
fruits=['mango', 'banana','orange', 'mango', 'mango']
while 'mango' in fruits:
    fruits.remove('mango')
print(fruits)
