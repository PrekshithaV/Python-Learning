# for loop 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# while loop

i = 1
while i < 6:
  print(i)
  i += 1


# Using for loop to print multiplication tables (1–5)

for i in range(1, 6):
    print("Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i*j)

    print()

# Using while loop to print multiplication tables (1–5)

i = 1

while i <= 5:
    print("Table of", i)

    j = 1
    while j <= 10:
        print(i, "x", j, "=", i*j)
        j += 1

    print()
    i += 1