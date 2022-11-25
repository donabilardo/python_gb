# Если одна из последовательностей будет меньше (по количеству элементов) 
# то ошибки не будет, а функция остановится когда дойдет до конца наименьшей последовательности
from a_list_сomprehension import getRandomList

listA = getRandomList()
listB = getRandomList()


listZip = zip(listA,listB)


print(f'Первый список: \n {listA} \n\n Второй список: \n {listB}\n\n {list(listZip)}')
