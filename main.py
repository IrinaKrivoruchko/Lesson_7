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

#2
while True:
    try:
        number = int(input("Enter number of stars: "))
        if number >= 1:
            break
        if number <= 0:
            print("You should to enter number more then 0")
    except ValueError:
        print("Enter only integer numbers please!")

def stars_in_row(num):
    if num >= 1:
        print("*", end='')
        return stars_in_row(num-1)

stars_in_row(number)