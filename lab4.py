import os, csv

class DataCollection:
    def __init__(self):
        # Инициализация пустого словаря для хранения данных
        self.data = {}

    def count_objects(self):
        dir_path = input("Enter directory path: ")
        # Подсчет количества объектов в директории
        folder_count = sum(len(files) for _, _, files in os.walk(dir_path))
        
        print(f"In folder {dir_path.split('/')[-1]} there are {folder_count} objects.")

    def write_to_csv(self):
        key_inp = input('Enter key: ')
        date_inp = input('Enter date: ')
        price_inp = input('Enter price: ')
        name_inp = input('Enter name: ')
        # Добавление новой записи в словарь
        self.data[key_inp] = [date_inp, price_inp, name_inp]
        # Запись данных в CSV-файл
        with open('for_lab3.csv', 'w') as f:
            for elem in self.data:
                f.write(elem + "," + self.data[elem][0] + "," + self.data[elem][1] + "," + self.data[elem][2] + "\n")

    def read_from_csv(self):
        # Чтение данных из CSV-файла и добавление их в словарь
        with open("for_lab3.csv", "r") as f:
            reader = csv.reader(f)
            for line in reader:
                self.data[line[0]] = line[1:]

    def sort_by_numeric_field(self):
        # Сортировка словаря по числовому полю и вывод отсортированных элементов
        print("Sorting the dictionary by price:")
        for elem in sorted(self.data.items(), key=lambda para: int(para[1][1])):
            print(elem[0], *elem[1])
        print("")

    def sort_by_string_field(self):
        # Сортировка словаря по строковому полю и вывод отсортированных элементов
        print("Sorting the dictionary by product name:")
        for elem in sorted(self.data.items(), key=lambda para: para[1][2]):
            print(elem[0], *elem[1])
        print("")

    def inference_by_criterion(self):
        print("Rows with product name 'pizza':")
        for elem in self.data:
            if self.data[elem][2] == 'pizza':
                # Вывод строк словаря, в которых наименование товара равно 'pizza'
                print(elem, *self.data[elem])

    def add_newline_to_file(self):
        check = input('Add newline to file? Enter y/n: ')
        if check == 'y':
            # Запись новой строки в файл
            self.write_to_csv()
            print("Data successfully saved!")
        else:
            print("Program stopped.")

    def __repr__(self):
        # Представление объекта в виде строки
        return repr(self.data)

    def __setattr__(self, name, value):
        if name != 'data':
            raise AttributeError(
                # Запрет прямого изменения атрибутов, использование 'data' атрибута
                "Cannot set attributes directly. Use 'data' attribute instead.")
        else:
            super().__setattr__(name, value)

    def __getitem__(self, key):
        # Возможность доступа к элементам коллекции по индексу
        return self.data[key]

    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass

    def __iter__(self):
        # Реализация итератора
        return iter(self.data)

def main():
    collection = DataCollection()
    collection.count_objects()
    collection.read_from_csv()

    print("ID, Date, Price, Product Name")
    for elem in collection:
        # Вывод данных из коллекции
        print(elem, *collection[elem])
    print("\n")

    collection.sort_by_numeric_field()
    collection.sort_by_string_field()
    collection.inference_by_criterion()
    print("")

    collection.add_newline_to_file()

if __name__ == "__main__":
    main()