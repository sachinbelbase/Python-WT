# import csv


# with open("student.csv", "r") as file:
#     reader = csv.reader(file)
#     print(reader)
#     for row in reader:
#         print(row)

# with open("student.csv", "r") as file:
#     reader = csv.DictReader(file)
#     print(reader,type(reader))
#     for row in reader:
#         print(row)
#         for key,value in row.items():
#             print(f'{key},:{value}')
       
       
            
# n =4;
# for x in range(n):
#         # y = x+1
#         # print("*" * y)
#         print("*" * (x+1))



# numbers = [int(x) for x in input("Enter a number:").split(",")]
# evensnum = [x for x in numbers if x % 2==0]
# print(evensnum)


students = {
        "Aarav":20,
        "Ram":92,
        "shyam": 92,
        "hari":30,
        "sita":50
}

# max_marks = max(students.values())
# print(max_marks)  

# top_student = max(students, key = students.get)
# print(top_student)

max_marks = max(students.values())
toppers = [name for name, marks in students.items() if marks == max_marks] 
print(toppers)

# students = {name: marks for name, marks in students.items() if marks > 40}
# print(students)
# def average_marks(marks):
#         total = 0
#         for mark in marks:
#                 total += mark
#         return total / len(marks)
# avg = average_marks(students.values())
# print(avg)