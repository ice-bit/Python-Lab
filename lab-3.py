Lab-3 adityasingh.24bpe098
1)Count how many vowels are there in a string. Accept the string from the user.
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in 'aeiouAEIOU':
            count += 1
    print("Vowels:", count)

count_vowels("Hello World")
2)Write your own functions (without using built-in functions) to convert all characters of a string into lower case / upper case / toggle case.
def to_lower(s):
    result = ''
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

def to_upper(s):
    result = ''
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result

def toggle_case(s):
    result = ''
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

print(to_lower("HeLLo"))
print(to_upper("HeLLo"))
print(toggle_case("HeLLo"))
3)Accept two strings. Check whether one string is there in another string.
def is_substring(s1, s2):
    if s1 in s2 or s2 in s1:
        print("Yes, one is in another")
    else:
        print("No, not found")

is_substring("test", "This is a test")
4)Write a function that removes one string from another string, if present.
def remove_string(main, remove):
    result = ""
    i = 0
    while i < len(main):
        if main[i:i+len(remove)] == remove:
            i += len(remove)
        else:
            result += main[i]
            i += 1
    print("Final String:", result)

remove_string("abcdef", "cd")
