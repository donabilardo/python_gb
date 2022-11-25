import re
from unittest import result

a = 'Скажика *дядя! Москва+спаленная пожаром!'

result = re.split('!| | *', a)

b = a.replace(' *','@')
b = b.replace('! ','@')
b = b.replace('+','@')
b = b.replace('!','@')
b = b.replace(' ','@')

c = b.split("!")

print(c)