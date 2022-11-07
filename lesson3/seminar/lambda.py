""" В файле хранятся числа, нужно выбрать
четные и составить список пар (число, квадрат числа)
Пример: 
123456789
Получить:
[{2,4},(8,64)]... """


from urllib.request import urlopen
html = urlopen('https://vk.com')
print(html.read())


