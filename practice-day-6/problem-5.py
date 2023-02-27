# python program to check Armstrong number
# method 1

# a = input()
# num_length = len(str(a))
# temp = a
# sum = 0

# while temp > 0:
#     lst_digit = temp%10
#     sum = sum + lst_digit**num_length
#     # temp = temp // 10
#     temp //= 10

# if sum == a:
#     print("Armstrong number")
# else:
#     print("not Armstrong")

# method 2

a = input() # 1 5 3
num_len = len(a)
sum = 0
for i in a:
    sum = sum + int(i)**num_len
    # sum += int(i)**num_len

if int(a) == sum:
    print("Armstrong")
else:
    print('Not Armstrong')