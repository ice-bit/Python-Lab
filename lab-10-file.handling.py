#Adityasingh.24bpe098

#1.	Write a program to create a csv file that we can directly open in MS-Excel.
import csv

data = [
    ['RollNo', 'Name', 'Maths', 'Science', 'English'],
    [1, 'Amit', 85, 78, 92],
    [2, 'Rina', 88, 91, 80],
    [3, 'Tom', 79, 84, 88]
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully!")

#2.	Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.
import csv

students_dict = {}

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = int(row['Maths']) + int(row['Science']) + int(row['English'])
        students_dict[row['Name']] = {
            'RollNo': row['RollNo'],
            'Maths': row['Maths'],
            'Science': row['Science'],
            'English': row['English'],
            'Total': total
        }

print(students_dict)

#3.	Accept contact details from the user and create a vcard that we can directly store in our mobile.
def create_vcard(name, phone, email, company):
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nORG:{company}\nEND:VCARD"
    with open(f"{name}_contact.vcf", "w") as file:
        file.write(vcard)

name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")
company = input("Enter company: ")

create_vcard(name, phone, email, company)
print(f"VCard for {name} created successfully!")

#4.	Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory.
import os
import shutil

subdirectory = 'new_subdirectory'
if not os.path.exists(subdirectory):
    os.makedirs(subdirectory)

source_file = 'source_subdirectory/sample.txt'
destination_file = os.path.join(subdirectory, 'sample.txt')

shutil.copy(source_file, destination_file)

print(f"File copied successfully to {destination_file}")

#5.	Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.
def copy_and_convert(source, destination):
    with open(source, 'r') as file:
        content = file.read()
    
    content = content.upper()

    with open(destination, 'w') as file:
        file.write(content)

source_file = 'source.txt'
destination_file = 'destination.txt'
copy_and_convert(source_file, destination_file)
print("File copied with content in uppercase.")

#6.	Write a program that merges lines alternatively from two files and writes the results to new file. If one file has less number of lines than the other,  the remaining lines from the larger file should be simply copied into the target file.
def merge_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    merged_lines = []
    for l1, l2 in zip(lines1, lines2):
        merged_lines.append(l1.strip() + "\n" + l2.strip() + "\n")

    longer_lines = lines1[len(lines2):] if len(lines1) > len(lines2) else lines2[len(lines1):]
    merged_lines.extend(longer_lines)

    with open(output_file, 'w') as output:
        output.writelines(merged_lines)

merge_files('file1.txt', 'file2.txt', 'merged_output.txt')
print("Lines merged successfully!")

#7.	If an Employee object contains following details: empcode, empname, Date of Joining, SalaryWrite a program to serialize and deserialize this data.
import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

employee = Employee(101, 'John Doe', '2024-05-01', 50000)
with open('employee.pkl', 'wb') as file:
    pickle.dump(employee, file)

print("Employee serialized successfully!")

with open('employee.pkl', 'rb') as file:
    employee = pickle.load(file)

print(f"Employee Name: {employee.empname}, Salary: {employee.salary}")

#8.	Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space.
def replace_words_in_file(input_file, output_file):
    words_to_replace = ['a', 'the', 'an']
    
    with open(input_file, 'r') as file:
        content = file.read()

    for word in words_to_replace:
        content = content.replace(f' {word} ', ' ')

    with open(output_file, 'w') as file:
        file.write(content)

    print("Words replaced and new file created.")

replace_words_in_file('input.txt', 'output.txt')
