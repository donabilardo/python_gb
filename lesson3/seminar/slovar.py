#словари

my_dict = {    
    'car' : 'машина',
    'color' : 'цвет',
    'red' : 'красного'
}


eng_text = "car red color"
rus_text = ""

for word in eng_text.split():
    if word in my_dict:
        rus_text += my_dict[word] + ' '


print(rus_text)