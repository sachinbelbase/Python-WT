# x=10
# y=20
# print("The value of x is %d and y is %d" %(x,y))

# case 4:
# name='Sachin'
# age=29
# print("The name is {x} and age is {y}".format(x = name, y= age))
# # print("The name is {0} and age is {1}".format(age, name))
# print("The name is {0} and age is {1}".format(name, age))

# # case 5:
# print(f'The value of name is {name}')

# FLow Control 

# x =10
# y =20
# z =30

# r = x if (x < y) and (x < z) else y if y > z else z
# print(r)

# name = input("Enter the name: ")

# if name.lower() == 'ncit':
#     print(f'Welcome to NCIT')

# else:
#     print('Welcome')


# score = int(input("Enter your score: "))

# if score>=90:
#     print(f'We got O and score is {score}')

# elif  90 > score>= 80:
#     print(f'You got A and score is {score}')
    
# elif  80 > score>= 70:
#     print(f'You got B and score is {score}')

# elif  70 >= score>= 60:
#     print(f'You got C and score is {score}')

# elif score>= 100:
#     print("Not Available")

# elif score< 60:
#     print('Fail')

# name = 'Sachin'
# for x in name[::2]:
#     print(x)
    
    
sum = 0
number = eval(input("Enter list of numbers: "))
for x in number:
    sum += x
print(sum)

