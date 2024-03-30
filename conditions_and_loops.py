# conditions

number = 11

if number == 11:
    print("something")


if number == 10:
    print(number)

# DRY (don't repeat yourself)
    
def number_check(number):
    if number == 11:
        print("number is 11")

    else:
        print("number is not 11")

number_check(12)

# loops

students = ["John", "Mark", "Venessa", "Mariam"]

print(students[0])

for student in students:
    print(student.upper())

# purpose define a function that do this:
    
# before: "hi may name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"
    
string = "hi my name is john and i am learning python"

def alternating(string):
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            string += string[string_index].upper()

        else:
            string += string[string_index].lower()
        
    print(string)

alternating(string)

# break & while & continue

salaries = [1000, 2000, 3000, 4000]

for salary in salaries:
    if salary == 1000:
        continue
    print(salary)
    if salary == 2000:
        break
        
number = 1 
while number < 5:
    print(number)
    number += 1

# enumerate
students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student) 

for index, student in enumerate(students):
    print(index)    

# divide students to two group according to index
    
def divide_students (students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)

        else:
            groups[1].append(student)
    print(groups)
    return groups

divide_students(students)

letter = len(string)
def alternating_with_enumarate(string):
    new_string = ""
    for index, letter in enumerate(string):
        if index % 2 == 0:
            new_string += letter.upper()

        else:
            new_string += letter.lower()
    
    print(new_string)

alternating_with_enumarate(string)

# zip

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

print(list(zip(students, departments, ages)))

# lambda, map, filter, reduce

# wtih lambda you don't need to define a fuction
def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b
new_sum(4, 5)

# map

def new_salary(x):
    return x * 20 /100 + x 

print(new_salary(1000))

# with map you don't need that for loop
for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))

# map lambda together
print(list(map(lambda x: x * 20 / 100 + x, salaries)))

# filter

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda x: x % 2 == 0, list_store)))

# reduce
from functools import reduce
list_store = [1, 2, 3, 4]

print(reduce(lambda a, b: a+ b, list_store))



