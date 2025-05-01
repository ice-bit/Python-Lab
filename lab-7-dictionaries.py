#Adityasingh.24bpe098
#1.	Write a program to create three dictionaries and concatenate them to create fourth dictionary.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}
dict4 = {**dict1, **dict2, **dict3}
print("Concatenated Dictionary:", dict4)

#2.	Write a program to check whether a dictionary is empty or not.
my_dict = {}

if not my_dict:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")

#3.	Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.
dept = {
    'HR': {'emp1': 3000, 'emp2': 5000, 'emp3': 4000},
    'IT': {'emp4': 8000, 'emp5': 7000, 'emp6': 9000},
    'Finance': {'emp7': 6000, 'emp8': 5500, 'emp9': 6500}
}

for department, employees in dept.items():
    min_salary = min(employees.values())
    max_salary = max(employees.values())
    print(f"Department: {department}, Min Salary: {min_salary}, Max Salary: {max_salary}")

#4.	Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string. 
input_string = input("Enter a string: ")

char_frequency = {}

for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Character Frequency Dictionary:", char_frequency)

#5.	Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.
prices = {'apple': 2, 'banana': 1, 'orange': 3, 'milk': 5}

quantities = {'apple': 4, 'banana': 3, 'orange': 2, 'milk': 1}

total_bill = 0
for item in prices:
    total_bill += prices[item] * quantities.get(item, 0)

print("Total Bill:", total_bill)
