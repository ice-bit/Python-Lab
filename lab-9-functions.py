#Adityasingh.24bpe098
#1.	If a positive integer is entered through the keyword, write a recursive function to obtain the prime factors of the number. 
def prime_factors(n, divisor=2):
    if n <= 1:
        return []
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)

# Test
num = int(input("Enter a positive integer: "))
print("Prime Factors:", prime_factors(num))

#2.	A positive integer is entered through the keyboard. Write a function to find its binary equivalent of this number.
def binary_equivalent(n):
    if n == 0:
        return "0"
    else:
        return binary_equivalent(n // 2) + str(n % 2)

# Test
num = int(input("Enter a positive integer: "))
print("Binary Equivalent:", binary_equivalent(num))

#3.	A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string.
def count_vowels(s, index=0, count=0):
    if index == len(s):
        return count
    if s[index].lower() in 'aeiou':
        count += 1
    return count_vowels(s, index + 1, count)

# Test
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))

#4.	Write a recursive function that reverses the list of numbers that it receives.
def reverse_list(lst):
    if len(lst) == 0:
        return lst
    else:
        return [lst[-1]] + reverse_list(lst[:-1])

# Test
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Reversed List:", reverse_list(numbers))

#5.	Calculate ab where a and b received through the keyword using recursion.
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

# Test
a = int(input("Enter base number (a): "))
b = int(input("Enter exponent number (b): "))
print(f"{a} raised to the power {b} is:", power(a, b))

#6.	A list contains some negative and some positive values. Write a recursive function that sanitizes the list by replacing all negative numbers with 0.
def sanitize_list(lst, index=0):
    if index == len(lst):
        return lst
    if lst[index] < 0:
        lst[index] = 0
    return sanitize_list(lst, index + 1)

# Test
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sanitized List:", sanitize_list(nums))

#7.	Write a recursive function to obtain average of all numbers present in a given list.
def average(lst, index=0, total=0):
    if index == len(lst):
        return total / len(lst) if len(lst) > 0 else 0
    total += lst[index]
    return average(lst, index + 1, total)

# Test
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Average:", average(numbers))

#8.	Write a recursive function to obtain length of a given string.
def string_length(s):
    if s == "":
        return 0
    else:
        return 1 + string_length(s[1:])

# Test
string = input("Enter a string: ")
print("Length of the string:", string_length(string))
