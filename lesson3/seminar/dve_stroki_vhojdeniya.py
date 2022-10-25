""" Пользователь задаёт две строки.
 Определить количество вхождений одной строки в другой. """

str1 = input("Первая строка : ")
str2 = input("Вторая строка : ")

def stringOccurrence(str1, str2):

    print(f'Введено в 1 строке: {str1}')
    print(f'Введено во 2 строке: {str2}')

    index = -1
    count = 0

    while index < len(str1):
        index = str1.find(str2, index+1)
        if index == -1:
            break
        count+= 1
    return count


print(f'Вхождений {stringOccurrence(str1,str2)}')