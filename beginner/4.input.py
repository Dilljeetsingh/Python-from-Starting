# input() = a function that prompts the user to enter data
#   return the entered data as a string

name = input("what is your name?; ")
age = int(input("how old are you?; "))

#age = int(age)
age = age + 1

print(f"hello {name}!")
print(f"happy birthday")
print(f"you are {age} years old")