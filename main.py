# #1 degree
# while True:
#     try:
#         x = int(input("Enter number: "))
#         if x > 0:
#             break
#         if x <= 0:
#             print("You should to enter number more then 0")
#     except ValueError:
#         print("Enter only integer numbers please!")
#
# while True:
#     try:
#         y = int(input("Enter degree: "))
#         if y >= 0:
#             break
#         if y < 0:
#             print("You should to enter number more then 0")
#     except ValueError:
#         print("Enter only integer numbers please!")
# # f(2,5)
# # 2*f(2,4)
# # 2*2*f(2,3)
# # 2*2*2*f(2,2)
# # 2*2*2*2*f(2,1)
# # 2*2*2*2*2*f(2,0)
# # 2*2*2*2*2*1

# def degree(a, b):
#     if b == 0:
#         return 1
#
#     return a * degree(a, b - 1)
#
# print(degree(x,y))

#2 stars
# while True:
#     try:
#         number = int(input("Enter number of stars: "))
#         if number >= 1:
#             break
#         if number <= 0:
#             print("You should to enter number more then 0")
#     except ValueError:
#         print("Enter only integer numbers please!")
#
# def stars_in_row(num):
#     if num >= 1:
#         print("*", end='')
#         return stars_in_row(num-1)
#якщо число не менше 1, тоді виводимо "*" і одразу викликаємо функцію, зменшуючи число на одиницю
#якщо число менше 1, тоді нічого не друкується і функція більше не викликається

# stars_in_row(number)

#3
checking = True
first_number = 0
second_number = 0

while checking:
    while True:
        try:
            first_number = int(input("Enter first number: "))
            break
        except ValueError:
            print("Enter only integer numbers please!")

    while True:
        try:
            second_number = int(input("Enter second number: "))
            break
        except ValueError:
            print("Enter only integer numbers please!")

    if first_number+1 == second_number or first_number == second_number:
        print("Enter please others numbers")
        print("the difference between the numbers should be larger")
    else:
        checking = False

temp = 0
if first_number > second_number:
    temp = first_number
    first_number = second_number
    second_number = temp

total_sum = 0
def sum_of_all_numbers(a, b, sum) -> int:

    if a < b:
        sum = a + sum_of_all_numbers(a+1, b, sum)
    return sum

print(f"Sum of all numbers beetween {first_number} and {second_number}: {sum_of_all_numbers(first_number + 1, second_number, total_sum)}")