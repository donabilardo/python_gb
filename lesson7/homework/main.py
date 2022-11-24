import csv

contact = {}

def display_contact():
    for user, phone in contact.items():
        print(f"Имя: {user}  Телефон: {phone}".center(5,"*"))

while True:
    choice = int(input(" 1. Добавить контакт \n 2. Найти контакт \n 3. Отобразить контакты\n 4. Редактировать контакт \n 5. Удалить контакт \n 6. Экспортировать контакты в CSV\n 8. Закрыть программу\n  Выберите цифру меню и нажмите Enter \n "))
    if choice == 1:
        name = input("Имя контакта\n")
        phone = input("Телефон контакта\n")
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
    elif choice == 6:
        with open("lesson7\homework\phonebook.csv", "w", encoding="utf-8", newline="") as phonebook:
            fieldname = ['name1', 'phone1']
            writer = csv.DictWriter(phonebook,fieldnames=fieldname)
            writer.writeheader()
            for name, phone in contact.items():
                writer = csv.writer(phonebook)
                writer.writerow([name, phone])
    else:
        break