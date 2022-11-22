import func

contact = {}

while True:
    menu = int(input("1. Добавить контакт \n 2. Найти контакт \n 3. Показать контакт \n 4. Редактировать кнотакт \n 5. Удалить контакт \n 6. Для выхода нажмите Enter "))
    if menu == 1:
        name1 = input("Фамилия контакта:  ")
        nameA = func.formatStr(name1)
        name2 = input("Имя контакта:  ")
        nameB = func.formatStr(name2)
        name3 = input("Отчество контакта:  ")
        nameC = func.formatStr(name3)
        fullname = func.joinStr(nameA, nameB, nameC)
        phone = input("Номер телефона:  ")
        phone = func.formatInt(phone)
        print(fullname)