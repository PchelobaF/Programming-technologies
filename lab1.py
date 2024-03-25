import random

def autolist(n: int) -> list:
    #Заполняем список рандомными числами от 0 до 99
    list_numbers = [random.randint(0, 100) for _ in range(n)]
    return list_numbers

def userlist() -> list:
    #Заполняем список вручную
    list_numbers = list(map(int, input("Введите целые числа (в одну строчку через пробел): ").split()))
    return list_numbers

def userlist_whithout() -> list:
    #Заполняем список вручную без использования стандартных функций
    n = int(input("Введите длину списка: "))
    list_numbers = []
    for _ in range(n):
        list_numbers += [int(input("Введите целое число: "))]
    return list_numbers

def del_min_num(start_chain: int, end_chain: int, list_numbers: list) -> None:
    # Удаляем минимальный элемент цепочки
    new_list = list_numbers[start_chain:end_chain]
    min_index = start_chain + new_list.index(min(new_list))
    del list_numbers[min_index]

def del_min_num_whithout(start_chain: int, end_chain: int, list_numbers: list) -> None:
    #Удаляем минимальный элемент цепочки без использования стандартных функций
    min_index = start_chain
    for j in range(start_chain + 1, end_chain):
        if list_numbers[j] < list_numbers[min_index]:
            min_index = j
    del list_numbers[min_index]

def find_chain(list_numbers: list) -> list:
    #Находим индексы начала и конца цепочки четных чисел
    i = 0
    while i < len(list_numbers):
        if list_numbers[i] % 2 == 0:
            start_chain = i
            while i < len(list_numbers) and list_numbers[i] % 2 == 0:
                i += 1
            end_chain = i
            del_min_num(start_chain, end_chain, list_numbers) 
        else:
            i += 1
    return list_numbers

def find_chain_whithout(list_numbers: list) -> list:
    #Находим индексы начала и конца цепочки четных чисел
    i = 0
    while i < len(list_numbers):
        if list_numbers[i] % 2 == 0:
            start_chain = i
            while i < len(list_numbers) and list_numbers[i] % 2 == 0:
                i += 1
            end_chain = i
            del_min_num_whithout(start_chain, end_chain, list_numbers) 
        else:
            i += 1
    return list_numbers

def main():
    while True:
        match input("Выберите способ заполнения списка:\n1.Автомотическое заполнение\n2.Ручное заполнение\n3.Выход\nВаш выбор: "):
            case "1":
                try:
                    list_numbers = autolist(int(input("Введите длину списка: ")))
                    break
                except ValueError:
                    print("Нужно ввести только число (буквы и символы нельзя)")
            case "2":
                match input("Выберите способ:\n1.Без использования стандартных функций\n2.С использованием стандартных функций\n3.Выход\nВаш выбор: "):
                    case "1":
                        list_numbers = userlist_whithout()
                        break
                    case "2":
                        list_numbers = userlist()
                        break
                    case "3":
                        break
                    case _:
                        print("Нет такого способа")
            case "3":
                break
            case _:
                print("Нет такого способа")

    while True:
        match input("Выберите способ работы метода:\n1.Без использования стандартных функций\n2.С использованием стандартных функций\n3.Выход\nВаш выбор: "):
            case "1":
                print(f"\nA[{len(list_numbers)}]: {list_numbers}")
                print("Вывод:\n\t ".replace(" ", " "*len(str(len(list_numbers)))), find_chain_whithout(list_numbers))
                break
            case "2":
                print(f"\nA[{len(list_numbers)}]: {list_numbers}")
                print("Вывод:\n\t ".replace(" ", " "*len(str(len(list_numbers)))), find_chain(list_numbers))
                break
            case "3":
                break
            case _:
                print("Нет такого способа")

if __name__ == "__main__":
    main()
