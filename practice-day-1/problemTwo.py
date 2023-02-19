first_num = int(input('please enter first number: '))
second_num = int(input('please enter second number: '))
third_num = int(input('please enter third number: '))

if first_num >= second_num and first_num >= third_num :
    print(first_num, "is largest")

elif second_num >= first_num and second_num >= third_num:
        print(second_num , "is largest")

elif third_num > first_num and third_num > second_num : 
    print(third_num , "is largest") 

# elif first_num == second_num or first_num == third_num or second_num == third_num:
#     print('Two numbers are equal in your input')

else: 
    print('All three numbers are equal')


# if first_num >= second_num:
#      if first_num >= third_num:
#           print(first_num, 'is the largest')
#      else:
#           print(third_num, 'is the largest')

# else:
#      if second_num >= third_num:
#           print(second_num, 'is the largest')
#      else:
#           print(third_num, 'is the largest')


    
