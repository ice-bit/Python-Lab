#Adityasingh.24bpe098

#1) Print all alphabets in upper case and in lower case.
def print_alphabets():
    for i in range(65, 91):
        print(chr(i), end=' ')
    print()
    for i in range(97, 123):
        print(chr(i), end=' ')

print_alphabets()

#2) Print a multiplication table of a given number.
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

table(5)

#3) Count no. of alphabets and no. of digits in any given string.
def count_alpha_digit(s):
    a = d = 0
    for ch in s:
        if ch.isalpha():
            a += 1
        elif ch.isdigit():
            d += 1
    print("Alphabets:", a)
    print("Digits:", d)

count_alpha_digit("abc123xy9")

#4) Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.
def check_properties(n):
    # Prime
    prime = True
    if n < 2:
        prime = False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break

    # Perfect
    perfect = sum(i for i in range(1, n) if n % i == 0) == n

    # Armstrong
    armstrong = sum(int(d)**len(str(n)) for d in str(n)) == n

    # Palindrome
    palindrome = str(n) == str(n)[::-1]

    # Automorphic
    automorphic = str(n*n).endswith(str(n))

    print("Prime:", prime)
    print("Perfect:", perfect)
    print("Armstrong:", armstrong)
    print("Palindrome:", palindrome)
    print("Automorphic:", automorphic)

check_properties(153)

#5) Generate all Pythagorean Triplets with side length <= 30.
def pythagorean_triplets():
    for a in range(1, 31):
        for b in range(a, 31):
            c = (a**2 + b**2)**0.5
            if c == int(c) and c <= 30:
                print(a, b, int(c))

pythagorean_triplets()

#6) Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
def print_24_hours():
    for h in range(24):
        if h == 0:
            print("12 Midnight")
        elif h == 12:
            print("12 Noon")
        elif h < 12:
            print(f"{h} AM")
        else:
            print(f"{h-12} PM")

print_24_hours()

#7) Print nCr and nPr.
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    return factorial(n) // factorial(n - r)

print("nCr:", nCr(5, 2))
print("nPr:", nPr(5, 2))

#8) Print factorial of a given number.
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    print("Factorial:", f)

fact(5)

#9) Print N natural nos. in reverse.
def reverse_n(n):
    for i in range(n, 0, -1):
        print(i, end=' ')

reverse_n(10)

#10) Generate N numbers of Fibonacci series.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10)

