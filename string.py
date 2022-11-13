# Showing small letter of hello changed to Hello
python_string= 'hellow this the sample string to show different method act on this'
test=python_string.capitalize()
print(test)

#Here it count how much time the t appers in given string
python_string= 'hellow this the sample string to show different method act on this'
test1=python_string.count('t')
print(test1)
# Showing small letter of hello changed to Hello
python_string= 'HELLOW this the sample string to show different METHODS act on this'
test=python_string.capitalize()
print(test)

lowe_case=python_string.casefold()
print(lowe_case)

print(python_string.center(14,'0'))
print(python_string.encode())
#Here it count how much time the t appers in given string
python_string= 'hellow this the sample string to show different method act on this'
test1=python_string.count('t')
print(test1)
print(python_string.endswith('s'))
# endswith method show a particular end in the string here we have -this- at the end so i entered s its gives true
# otherwise its false

print(python_string.expandtabs(10))
print(python_string.find('e'))
# here in find we albe to find the position of e its in at 1 index as we all kon index start from 0
print(python_string.format('s'))
print(python_string.format_map('s'))
print(python_string.index('this'))
print(python_string.isalnum())
print(python_string.isalpha())
#here its also condidering the white spaces so showes as false
print(python_string.isascii())
print(python_string.isdecimal())
print(python_string.isdigit())
print(python_string.isidentifier())
print(python_string.isprintable())
print(python_string.istitle())
#its returns true if all letters ofeach word at staring is capital
print(python_string.title())
#here the above method convert each starting letters to capital or upper case
print(python_string.upper())
print(python_string.rfind('sample'))
print(python_string.partition('sample'))
