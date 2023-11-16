# ввести 2 числа и определить какое из них больше

# first = int(input("first digit "))
# second = int(input("second digit "))

# if first > second:
#     print(f"first = {first} > second = {second}")

# elif first == second:
#     print(f"first = {first} == second = {second}")

# else:
#     print(f"first = {first} < second = {second}")            

# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# firstClass = int(input("Кол-во человек в первом классе "))
# secondClass = int(input("Кол-во человек во втором классе "))
# thirdClass = int(input("Кол-во человек в третьем классе "))

# schoolDesk1 = firstClass // 2 + (firstClass % 2 != 0) #условие выдает true (единица) или false (ноль), чтобы решение было универсальное на любое кол-во мест за партой
# schoolDesk2 = secondClass // 2 + (secondClass % 2 != 0)
# schoolDesk3= thirdClass // 2 + (thirdClass % 2 != 0)

# schoolDeskAll = schoolDesk1 + schoolDesk2 + schoolDesk3

# print(f"Кол-во парт = {schoolDeskAll}")



# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:

# n = int(input("Машина проезжает за день -  "))
# m = int(input("Длинна маршрута -  "))

# d = (m // -n)

# print(f"Проедет за {-d} дней")


# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES


year = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:

    print("Год високосный")

else:

    print("Год не високосный")



# Задача №5. Общее обсуждение
# 5.Вагоны в электричке пронумерованы
# натуральными числами, начиная с 1 (при этом иногда
# вагоны нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6