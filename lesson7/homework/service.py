contact = {}


def display_contact():
    print(contact.items())
    print("Имя\t\tТелефон")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


while True:
    choice = int(input(" 1. Добавить контакт \n 2. Найти контакт \n 3.Отобразить контакты\n 4. Редактировать контакт \n 5. Удалить контакт \n 6. Экспортировать контакты\n 7.Закрыть программу\n Выберите цифру меню и нажмите Enter "))
    if choice == 1:
        name = input("Имя контакта ")
        phone = input("Телефон контакта")
        contact[name] = phone
    elif choice == 2:
        search_name = input(" \n Имя контакта для поиска  \n ")
        if search_name in contact:
            print(search_name,"'Номер контакта ",contact[search_name])
        else:
            print("Такого контакта не найдено")
    elif choice == 3:
        if not contact:
            print(" \n Адресная книга пуста \n")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input(" \n Имя контакта для редактирования \n  ")
        if edit_contact in contact:
            phone = input(" \n Номер телефона \n ")
            contact[edit_contact]=phone
            print(" \n Контакт обновлен \n ")
            display_contact()
        else:
            print(" \n Контакт не найден в адресной книге \n ")
    elif choice == 5:
        del_contact = input(" \n Имя контакта для удаления \n  ")
        if del_contact in contact:
            confirm = input(" \n Подтвердите удаление контакта Д или Н \n  ")
            if confirm =='д' or confirm =='Д':
                contact.pop(del_contact)
            display_contact()
        else:
            print("\n Контакт не найден в адресной книге \n")
    else:
        break