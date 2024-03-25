import os, csv

def dpath() -> (bool, bool, str):
	#Добавление пути до папки
	dir_path = input("Введите путь к папке в которой хотите узнать кол-во файлов: ")
	if os.path.exists(dir_path):
		print("Путь к папке успешно добавлен")
		return True, True, dir_path
	else:
		print("Нет такой папки!!!")
		return vibor(), False, None

def fpath() -> (bool, bool, str):
	#Добавление пути до файла
	file_path = input("Введите путь к csv файлу (включая сам файл): ")
	if os.path.isfile(file_path):
		print("Путь к файлу успешно добавлен")
		return False, True, file_path
	else:
		print("По этому пути нет файла")
		return vibor(), False, None

def vibor() -> int:
	#Выбор пользователя ввести путь заново или выйти из программы
	try:
		v = int(input("1.Ввести заново\n2.Выход\nВаш выбор: "))
		if v == 1:
			return True
	except ValueError:
		print("Нужно ввести только число (буквы и символы нельзя)")
	return False

def count_files_in_dir(dir_path: str) -> int:
	#Подсчет количества файлов в директории
    return sum(len(files) for _, _, files in os.walk(dir_path))

def read_data_from_csv(file_path: str) -> list:
	data = {}
	# Чтение данных из CSV-файла и добавление их в словарь
	with open(file_path, "r") as f:
		reader = csv.reader(f)
		for line in reader:
			data[line[0]] = line[1:]
	return data

def sort_by_numeric_field(data: dict):
	# Сортировка словаря по числовому полю и вывод отсортированных элементов
	print("Sorting the dictionary by price:")
	for elem in sorted(data.items(), key=lambda para: int(para[1][1])):
		print(elem[0], *elem[1])
	print("")

def sort_by_string_field(data: dict):
	# Сортировка словаря по строковому полю и вывод отсортированных элементов
	print("Sorting the dictionary by product name:")
	for elem in sorted(data.items(), key=lambda para: para[1][2]):
		print(elem[0], *elem[1])
	print("")

def inference_by_criterion(data: dict):
	print("Rows with product name 'pizza':")
	for elem in data:
		if data[elem][2] == 'pizza':
			# Вывод строк словаря, в которых наименование товара равно 'pizza'
			print(elem, *data[elem])

def write_data_to_csv(data: list, file_path: str) -> None:
	#Запись данных в CSV файл
	try:
		key_inp = input('Enter key: ')
		date_inp = input('Enter date: ')
		price_inp = input('Enter price: ')
		name_inp = input('Enter name: ')
		# Добавление новой записи в словарь
		data[key_inp] = [date_inp, price_inp, name_inp]
		# Запись данных в CSV-файл
		with open(file_path, 'w') as f:
			for elem in data:
				f.write(elem + "," + data[elem][0] + "," + data[elem][1] + "," + data[elem][2] + "\n")
	except PermissionError:
		print("Открытый файл!\nНевозможно обновить данные")

def add_newline_to_file(data: list, file_path: str):
	check = input('Add newline to file? Enter y/n: ')
	if check == 'y':
		# Запись новой строки в файл
		write_data_to_csv(data, file_path)
		print("Data successfully saved!")
	else:
		print("Program stopped.")

def main(dir_path: str, file_path: str) -> None:
	print(f"Кол-во файлов в папке {dir_path.split('/')[-1]} = {count_files_in_dir(dir_path)}")
	data = read_data_from_csv(file_path)
	print(f"В файле {file_path.split('/')[-1]} находятся данные:\n")
	print("ID, Date, Price, Product Name")
	for elem in data:
		# Вывод данных из коллекции
		print(elem, *data[elem])
	print()
	sort_by_numeric_field(data)
	sort_by_string_field(data)
	inference_by_criterion(data)
	add_newline_to_file(data, file_path)

if __name__ == '__main__':
	v = True
	d, f = False, False
	while v:
		if not f and d:
			v, f, file_path = fpath()

		if not d:
			v, d, dir_path = dpath()
	if d and f:
		main(dir_path.replace('\\', "/"), file_path.replace('\\', "/"))	