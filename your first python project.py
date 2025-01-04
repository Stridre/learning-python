#age is a variable and in this situation it is used as a variable for the input in he question "how old are you"
#age = int(age) is a way of changing the type of the variable (in this case its age)
# age += (1) means you add 1 to the interger that the user will input, if the type of the variable is string, the output will be (your input)1, and not (your input)+1
#print(f""{}") is used to output the user input of age while also saying something before or after the output
age = input("how old are you")
age = int(age)
age += (1)
print(f"you are {age} years old next year")