# ввести 2 числа и определить какое из них больше

# first = int(input("first digit "))
# second = int(input("second digit "))

# if first > second:
#     print(f"first = {first} > second = {second}")

# elif first == second:
#     print(f"first = {first} == second = {second}")

# else:
#     print(f"first = {first} < second = {second}")            


firstClass = int(input("Кол-во человек в первом классе "))
secondClass = int(input("Кол-во человек во втором классе "))
thirdClass = int(input("Кол-во человек в третьем классе "))

schoolDesk1 = firstClass // 2 + firstClass % 2
schoolDesk2 = secondClass // 2 + secondClass % 2
schoolDesk3= thirdClass // 2 + thirdClass % 2

schoolDeskAll = schoolDesk1 + schoolDesk2 + schoolDesk3

print(f"Кол-во парт = {schoolDeskAll}")

# n = int(input("Машина проезжает за день -  "))
# m = int(input("Длинна маршрута -  "))

# d = (m // -n)

# print(f"Проедет за {-d} дней")