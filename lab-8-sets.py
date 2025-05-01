#Adityasingh.24bpe098

#1.	Write a program that converts words present in a list into uppercase and stores them in a set.
words = ['apple', 'banana', 'grape', 'kiwi', 'mango']

uppercase_words = {word.upper() for word in words}

print("Set of Uppercase Words:", uppercase_words)

#2.	Write a program to create a set containing 10 random numbers in the range 15 to 45. Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.
import random

random_numbers = {random.randint(15, 45) for _ in range(10)}
print("Random Numbers:", random_numbers)

less_than_30 = len([num for num in random_numbers if num < 30])
print("Numbers less than 30:", less_than_30)

random_numbers = {num for num in random_numbers if num <= 35}

print("After Deleting Numbers > 35:", random_numbers)

#3.	Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it.
names = set()

names.add("John")
names.add("Alice")
names.add("Bob")
names.add("Charlie")
names.add("David")

print("Set after adding names:", names)

names.remove("Bob")
names.add("Benjamin")

names.remove("Alice")
names.remove("Charlie")

print("Set after modification and deletion:", names)

#4.	A set contains names which begin either with A or with B. Write a program to separate out the names into two sets, one containing names beginning with A and another with B.
names = {"Alice", "Bob", "Aaron", "Bella", "Charles", "Annie", "Bruce"}

set_A = {name for name in names if name.startswith('A')}
set_B = {name for name in names if name.startswith('B')}

print("Names starting with A:", set_A)
print("Names starting with B:", set_B)
