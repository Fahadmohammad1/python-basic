# longcut method
a = int(input('Enter your number'))

count = 0

while a> 0:
    count = count + 1
    a = a//10
print(count)

#shortcut method
b = input()
print(len(b))