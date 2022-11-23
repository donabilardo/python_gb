import csv


def export_phonebook(dict_phonebook):
    phonebook = "lesson7\homework\phonebook.csv"
    with open(phonebook, "w", newline="", encoding="utf-8") as file:
        columns = ["Имя", "Телефон"]
        writer = csv.DictWriter(file),#fieldnames=columns)
        writer.writeheader()
        for i in range(len(dict_phonebook)):
            writer.writerow(dict_phonebook)

