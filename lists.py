# create a list

mylist = ["apple", "banana", "cherry"]
print(mylist)

# list length

thelist = ["apple", "banana", "cherry"]
print(len(thelist))

# allow duplicate

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# access

mylist = ["apple", "orange", "cherry"]
print(mylist[1])


# PRACTICE - list slicing, append, remove, sort on a list of 10 numbers


# Creating a list of 10 numbers
numbers = [45, 12, 78, 23, 56, 9, 34, 67, 89, 21]

print("Original List:", numbers)

# List slicing
print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[5:])
print("Elements from index 2 to 6:", numbers[2:7])

# Append an element
numbers.append(100)
print("After append:", numbers)

# Remove an element
numbers.remove(23)
print("After remove:", numbers)

# Sort the list
numbers.sort()
print("After sorting:", numbers)