# Creating Variables

x = "hello"
y= "world"
print(x)
print(y)

# Casting 

x = str(3)
y = int(3)
z = float(3)
print(x, y, z)

# get the type

x = 5
y = "prekshi"
print(type(x))
print(type(y))

# one value to multiple variables

x = y = z = "apple"
print(x)
print(y)
print(z)

# global variables

x = "awesome"
def myfunc():
    print("Python is" + x)
myfunc()


# PRACTICE - create 5 variables (string, int, float, list, dict) and print them

name = "Prekshitha"
age = 19
height = 5.6
skills = ["Python", "AI", "SQL"]
student = {
    "name": "Prekshitha",
    "department": "AI & DS"
}                        

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Skills:", skills)
print("Student Details:", student) 