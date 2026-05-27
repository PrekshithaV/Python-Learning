# creating a function

def myfunc():
    print("hello friends")
myfunc()

def happy_birthday():
    print("happy birthday to you!")
    print("you are old!")
    print("happy birthday to you!")
happy_birthday()

# arguments

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due:{due_date}")
display_invoice("Prekshi", "100.00", "01/10")


# PRACTICE - write 3 functions — add two numbers, find max of a list, count words in a sentence

def add(a, b):
    return a + b

def biggest(numbers):
    return max(numbers)

def word_count(sentence):
    words = sentence.split()
    return len(words)


print(add(5, 3))
print(biggest([2, 8, 1, 10, 4]))
print(word_count("Python is very easy"))