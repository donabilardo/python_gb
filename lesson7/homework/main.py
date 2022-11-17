import func

contact = {}

while True:
    menu = int(input("1. Добавить контакт \n 2. Найти контакт \n 3. Показать контакт \n 4. Редактировать кнотакт \n 5. Удалить контакт \n 6. Для выхода нажмите Enter "))
    if menu == 1:
        name1 = input("Фамилия контакта")
        name1 = name1(func.formatStr(name1))
        name2 = input("Имя контакта")
        name2 = name2(func.formatStr(name2))
        name3 = input("Отчество контакта")
        name3 = name3(func.formatStr(name3))


