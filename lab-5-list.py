#Adityasingh.24bpe098
#1. Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos. Replace the third element of odd integers with a list of 4 even integers. Flattern, sort
#and print the list. Provide appropriate message at each stage.
import random

odd_list = random.sample(range(1, 100, 2), 5)
print("Original Odd List:", odd_list)

even_list = random.sample(range(0, 100, 2), 4)
print("Even List:", even_list)

odd_list[2] = even_list
print("After Replacing 3rd Element:", odd_list)

flat_list = []
for i in odd_list:
    if isinstance(i, list):
        flat_list.extend(i)
    else:
        flat_list.append(i)

flat_list.sort()
print("Flattened & Sorted List:", flat_list)


#2. Generate 20 random integers and store them in a list. Accept a number from the user and print#position of all occurrences of that number in the list.
import random

nums = [random.randint(1, 10) for _ in range(20)]
print("Generated List:", nums)

n = int(input("Enter number to find: "))
positions = [i for i, val in enumerate(nums) if val == n]
print("Positions:", positions)

#3. Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.
import random

nums = [random.randint(1, 30) for _ in range(50)]
print("Original List:", nums)

unique = list(set(nums))
print("Without Duplicates:", unique)

#4. Generate 30 random numbers and put them in a list. Create two more lists – one containing only# ve numbers and another with –ve nos.
import random

nums = [random.randint(-50, 50) for _ in range(30)]
print("All Numbers:", nums)

positives = [x for x in nums if x >= 0]
negatives = [x for x in nums if x < 0]

print("Positive Numbers:", positives)
print("Negative Numbers:", negatives)

#5. A list contains 5 strings. Convert all these strings to uppercase.
words = ['apple', 'banana', 'grape', 'kiwi', 'mango']
upper_words = [word.upper() for word in words]
print("Uppercase Words:", upper_words)

#6. Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
f = [32, 50, 77, 104, 122]
c = [(temp - 32) * 5/9 for temp in f]
print("Temperatures in Celsius:", c)

#7. Write a menu-driven program to implement the stack data structure.
stack = []

while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        ele = input("Enter element to push: ")
        stack.append(ele)
    elif choice == 2:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is Empty!")
    elif choice == 3:
        print("Stack:", stack)
    elif choice == 4:
        break

#8. Write a menu-driven program to implement the Queue data structure.
queue = []

while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        ele = input("Enter element to enqueue: ")
        queue.append(ele)
    elif choice == 2:
        if queue:
            print("Dequeued:", queue.pop(0))
        else:
            print("Queue is Empty!")
    elif choice == 3:
        print("Queue:", queue)
    elif choice == 4:
        break

#9. Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2 nd list (use list comprehension).
 list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

result = [x for x in list1 if x not in list2]

print("List1:", list1)
print("List2:", list2)
print("Result:", result)

