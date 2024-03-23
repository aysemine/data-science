#define integer variable and check the type
x = 46
print(type (x))

#convert integer to float
print(type(float(x)))

#string
string = "hello"
print(type(string))

#find spesific index in string
print(string[0])

#multiple index
print(string[0:2])

#check for characters in string
print("hell" in string)

#string methods
#for finding different methods dir(str)

#find the length of string
print(len(string))

#make string upper-lowercase
print(string.upper(), string.lower())

#replace characters from string
print(string.replace("lo", "p"))

#split strings
string = "hello World"
print(string.split())

#strip strings
print(string.strip("hello "))

#capitalize the first letter
print(string.capitalize())

#lists
notes = [1, 2, 3, 4, "note", True, [6, 7]]
print(type(notes))
print(notes[6][1])
print(notes[0:3])
notes.append(10)
notes.pop(0)
notes.insert(2, 99)
print(notes)

#dictionary
#key-value
dictionary =  {"REG": "Regression",
               "LOG": ["Logistic Regression", 20]}

print(dictionary["REG"])
print(dictionary["LOG"][1])
print("REG" in dictionary)
print(dictionary.get("LOG"))
dictionary.update({"REG": 11})
dictionary.update({"RF": 30})
print(dictionary)

#tuple (you can't change/update the tuple, thats makes it secure)
tuple = ("Masayoshi", "Takanaka")
print(tuple)

#set
set1 = set([1, 2, 3, 4])
set2 = set([1, 2, 3, 5])
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.isdisjoint(set2))


