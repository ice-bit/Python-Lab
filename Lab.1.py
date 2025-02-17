# Question - 1
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Addition:", a + b)

# Question - 2
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Subtraction:", a - b)

# Question - 3
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Multiplication:", a * b)

# Question - 4
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if b != 0:
 print("Division:", a / b)
else:
 print("Division by zero is not allowed")

# Question - 5
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if b != 0:
 print("Addition:", a + b)
 print("Subtraction:", a - b)
 print("Multiplication:", a * b)
 print("Division:", a / b)
else:
 print("Division by zero is not allowed")

# Question - 6
hours = float(input("Enter hours: "))
print("Minutes:", hours * 60)

# Question - 7
minutes = float(input("Enter minutes: "))
print("Hours:", minutes / 60)

# Question - 8
dollars = float(input("Enter dollars: "))
print("Rupees:", dollars * 48)

# Question - 9
rupees = float(input("Enter Rupees: "))
print("Dollars:", rupees / 85)

# Question - 10
dollars = float(input("Enter dollars: "))
rupees = dollars * 85
pounds = rupees / 105
print("Pounds:", pounds)

# Question - 11
grams = float(input("Enter grams: "))
print("Kilograms:", grams / 1000)

# Question - 12
kgs = float(input("Enter kilograms: "))
print("Grams:", kgs * 1000)

# Question - 13
bytes_val = float(input("Enter bytes: "))
print("Kilobytes:", bytes_val / 1024)
print("Megabytes:", bytes_val / (1024 ** 2))
print("Gigabytes:", bytes_val / (1024 ** 3))

# Question - 14
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (9 / 5 * celsius) + 32
print("Fahrenheit:", fahrenheit)

# Question - 15
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = 5 / 9 * (fahrenheit - 32)
print("Celsius:", celsius)

# Question - 16
P = float(input("Enter Principal: "))
R = float(input("Enter Rate of interest: "))
N = float(input("Enter Time (in years): "))
interest = (P * R * N) / 100
print("Interest:", interest)

# Question - 17
L = float(input("Enter the side length of the square: "))
print("Area:", L ** 2)
print("Perimeter:", 4 * L)

# Question - 18
L = float(input("Enter the length of the rectangle: "))
B = float(input("Enter the breadth of the rectangle: "))
print("Area:", L * B)
print("Perimeter:", 2 * (L + B))

# Question - 19
R = float(input("Enter the radius of the circle: "))
print("Area:", (22 / 7) * R ** 2)

# Question - 20
H = float(input("Enter the height of the triangle: "))
L = float(input("Enter the base length of the triangle: "))
print("Area:", (H * L) / 2)

# Question - 21
gross_salary = float(input("Enter gross salary: "))
allowances = gross_salary * 0.1
deductions = gross_salary * 0.03
net_salary = gross_salary + allowances - deductions
print("Net Salary:", net_salary)

# Question - 22
gross_sales = float(input("Enter gross sales: "))
discount = gross_sales * 0.1
net_sales = gross_sales - discount
print("Net Sales:", net_sales)

# Question - 23
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
total = sub1 + sub2 + sub3
average = total / 3
print("Total Marks:", total)
print("Average Marks:", average)

# Question - 24
x = input("Enter the first value: ")
y = input("Enter the second value: ")
print("Before Swap: x =", x, ", y =", y)
x, y = y, x
print("After Swap: x =", x, ", y =", y)
