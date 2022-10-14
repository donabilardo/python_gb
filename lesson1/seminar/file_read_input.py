# -*- coding: utf-8 -*-
#запись и чтение данных с файлов 
from random import randint
from unittest.mock import patch

n = 10
random_list = []
for i in range(n):
    random_list.append(randint(-100,100))

#print(random_list)

path_file = "lesson1\\seminar\\newfile.txt"


f = open("lesson1\\seminar\\newfile.txt", 'a',encoding='utf-8')
f.writelines('Тестовая строка \n')
f.close()


data = open(path_file, 'r', encoding='utf-8')
for i in data:
    print(i)
data.close()


exit() #после этого метода, программа игнорируетпоследующий код