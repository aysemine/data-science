# define function

def calculate(x):
    print(x*2)

calculate(5)

def summer(arg1, arg2):
    print(arg1 + arg2)

summer(7, 8)

# docstring

def summer(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float

    """
    print(arg1 + arg2)

# def funciton_name(parameters/args):
#   statement (function body)
    
def multiplication(a, b):
    c = a * b
    print(c)

multiplication(10, 9)

list_store = []

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1, 8)

def divide(a, b = 1):
    print(a / b)

divide(1)

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

varm, moisture, charge, output = calculate(98, 12, 78)

print(charge)

# local ¾ global variables

list_store = [1, 2]

def add_element(a, b):
    c = a * b 
    list_store.append(c)
    print(list_store)

add_element(1, 9)
print(c)
