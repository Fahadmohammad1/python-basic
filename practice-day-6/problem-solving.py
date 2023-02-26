# #namta print

# a = int(input("Enter a number : "))
# for i in range(1, 11):
#     print(a, 'X', i , '=', a*i )

num = int(input('input a number : '))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print(factorial)