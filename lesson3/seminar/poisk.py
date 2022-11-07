num = '234'

elem = ['234','266','222','555', '234']


def checkNumber (num, elem):
    count = 0
    for i in elem:
        if i == num:
            return True
    return False


if checkNumber(num,elem):
    print(f'Число {num} присутствует {checkNumber(num,elem)}')
else:
    print(f'Число {num} не присутствует')