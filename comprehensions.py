# list comprehensions

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x 

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

# with list comprehensions you don't need that much steps
    
[salary * 2 for salary in salaries ]

# if you write only if then it needs to be in the last
[salary * 2 for salary in salaries if salary < 3000]

# if you use if-else together then it needs to be in the first
[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

[student.lower() if student in students_no else students.upper() for student in students ]

[student.lower() if student not in students_no else students.upper() for student in students ]

# dict comprehensions

dictionary= {'a': 1,
             'b': 2,
             'c': 3,
             'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k : v ** 2 for (k, v) in dictionary.items()}
{k.upper() : v ** 2 for (k, v) in dictionary.items()}