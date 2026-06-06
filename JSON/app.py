import json

# Load
# 1.
# with open(r"JSON\demo.json", "r") as file:
#     data = json.load(file)
    
# 2.
# def get_salary(employess):
#     return employess["age"]

# high_age = max(data["employees"],key=get_salary)

# print(high_age['Name'])
# print(high_age['age'])


# 3.
# Dump
# demo={
#   "name": "Sachin",
#   "age": 18,
#   "subjects": ["Web Technology II", "DSA", "DBMS"],
#   "address": {
#     "city": "Kathmandu",
#   }
# }

# with open("JSON\\demo.json", "w") as file:
#     json.dump(demo, file, indent=5)
#     print(type(demo))
    

# with open("JSON\demo.json", "r") as file:
#     data = file.read()
#     data = json.loads(data)
# print(data)


# Dumps
# demo={
#   "name": "Sachin",
#   "age": 18,
#   "subjects": ["Web Technology II", "DSA", "DBMS"],
#   "address": {
#     "city": "Kathmandu"
#   }
# }

# with open(r"JSON\demo.json", "w") as file:
#     data = json.dumps(demo, indent=5)
#     file.write(data)
#     # print(type(demo))