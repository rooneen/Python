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

firstClass = int(input("Кол-во человек в первом классе "))
secondClass = int(input("Кол-во человек во втором классе "))
thirdClass = int(input("Кол-во человек в третьем классе "))

schoolDesk1 = firstClass // 2 + (firstClass % 2 != 0) #условие выдает true (единица) или false (ноль), чтобы решение было универсальное на любое кол-во мест за партой
schoolDesk2 = secondClass // 2 + (secondClass % 2 != 0)
schoolDesk3= thirdClass // 2 + (thirdClass % 2 != 0)

schoolDeskAll = schoolDesk1 + schoolDesk2 + schoolDesk3

print(f"Кол-во парт = {schoolDeskAll}")



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