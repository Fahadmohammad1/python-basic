# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i*j, end = " ")
#     print()

# a = 0
# b = 0
# while a <= 5:
#     a = a + 1
#     while b <= 5:
#         b = b + 1
#     print(a*b, end= " ")

# for row in range(3):
#     for col in range(row + 1):
#         print("#" , end= " ")
#     print()

for row in range(3):
    for col in range(row + 1):
        print(chr(97+row) , end= " ")
    print()