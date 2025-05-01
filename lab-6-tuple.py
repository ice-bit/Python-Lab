##Adityasingh.24bpe098
#1.	A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))
people = [("Raj", "Amit"), "Rina", ("Tom", "Sam"), "Sita", "Mona"]

boys = 0
girls = 0

for p in people:
    if isinstance(p, tuple):
        boys += len(p)
    else:
        girls += 1

print("Number of Boys:", boys)
print("Number of Girls:", girls)

#2.	A list contains tuples containing roll no., name and age of student. Write a python program to create three lists separately for roll no., name and age
students = [(101, "Amit", 18), (102, "Rina", 19), (103, "Tom", 17)]

roll_nos = []
names = []
ages = []

for stu in students:
    roll_nos.append(stu[0])
    names.append(stu[1])
    ages.append(stu[2])

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)

#3.	Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.
import datetime

date1 = (2, 5, 2024)
date2 = (10, 6, 2024)

d1 = datetime.date(date1[2], date1[1], date1[0])
d2 = datetime.date(date2[2], date2[1], date2[0])

diff = abs((d2 - d1).days)
print("Number of Days Between:", diff)

#4.	Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.
food = [("Burger", 99), ("Pizza", 149), ("Fries", 60), ("Soda", 40)]

sorted_food = sorted(food, key=lambda x: x[1], reverse=True)

print("Sorted by Price (Descending):", sorted_food)

#5.	Remove empty tuple(s) from the list of tuples.
tlist = [(), (1, 2), (), (3,), (), (4, 5)]

cleaned = [t for t in tlist if t]

print("List after removing empty tuples:", cleaned)

#6.	Modify an element of a tuple.
t = (10, 20, 30)
print("Original Tuple:", t)

# Modify 2nd element to 99
t = t[:1] + (99,) + t[2:]

print("Modified Tuple:", t)

#7.	Delete an element of a tuple.
t = (1, 2, 3, 4)
print("Original Tuple:", t)

# Remove element at index 1
t = t[:1] + t[2:]

print("After Deletion:", t)

