def display_list_details(lst):
    print("\n--- LIST DETAILS ---")
    print("List:", lst)
    print("Length:", len(lst))
    print("First Element:", lst[0])
    print("Last Element:", lst[-1])
    print("Sliced (1:4):", lst[1:4])



my_list = [11, 2, 3, "ARTIFICIAL INTELLIGENCE", 45.6]
display_list_details(my_list)

print("\nUsing Enumerate:")
for index, item in enumerate(my_list):
    print(f"Index {index} → {item}")


my_list.append(100)
my_list.insert(1, "AI")
my_list.extend([200, 300])
print("\nAfter Append, Insert, Extend:", my_list)


try:
    my_list.remove("ARTIFICIAL INTELLIGENCE")
    removed_item = my_list.pop(1)
    print("Popped Item:", removed_item)
except ValueError:
    print("Item not found!")

print("After Modifications:", my_list)


numbers_only = [x for x in my_list if isinstance(x, (int, float))]
numbers_only.sort()
print("\nSorted Numeric Values:", numbers_only)


nested = [[1, 2], [3, 4], [5, 6]]
print("\nNested List Values:")
for row in nested:
    for value in row:
        print(value)

#display list details
def display_list_details(lst):
    print("\n--- LIST DETAILS ---")
    print("List:", lst)
    print("Length:", len(lst))
    print("First Element:", lst[0])
    print("Last Element:", lst[-1])
    print("Sliced (1:4):", lst[1:4])


my_list = [11, 2, 3, "ARTIFICIAL INTELLIGENCE", 45.6]
display_list_details(my_list)


print("\nUsing Enumerate:")
for index, item in enumerate(my_list):
    print(f"Index {index} → {item}")


my_list.append(100)
my_list.insert(1, "AI")
my_list.extend([200, 300])
print("\nAfter Append, Insert, Extend:", my_list)


try:
    my_list.remove("ARTIFICIAL INTELLIGENCE")
    removed_item = my_list.pop(1)
    print("Popped Item:", removed_item)
except ValueError:
    print("Item not found!")

print("After Modifications:", my_list)


numbers_only = [x for x in my_list if isinstance(x, (int, float))]
numbers_only.sort()
print("\nSorted Numeric Values:", numbers_only)


nested = [[1, 2], [3, 4], [5, 6]]
print("\nNested List Values:")
for row in nested:
    for value in row:
        print(value)

#List Comprehension 
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print("\nSquares:", squares)


pairs = [(x, y) for x in range(3) for y in range(3)]
print("Pairs:", pairs)


tuple1 = (11, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print("\nAdded Tuple:", new_tuple)


print("Tuple Elements:")
for item in new_tuple:
    print(item)

num = int(input("\nEnter number to check in tuple: "))
if num in new_tuple:
    print(num, "is present in tuple")
else:
    print(num, "not present")


student = {
    "name": "Ratchita",
    "course": "AI",
    "marks": 95
}

print("\nDictionary Data:")
for key, value in student.items():
    print(key, ":", value)


value = int(input("\nEnter a value: "))

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Number is:", check(value))

if value < 5:
    print("Less than 5")
elif value == 10:
    print("Value is 10")
else:
    print("Greater than 5")


if value > 5:
    if value < 20:
        print("Value is between 5 and 20")
    else:
        print("Value is 20 or more")
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print("\nSquares:", squares)

pairs = [(x, y) for x in range(3) for y in range(3)]
print("Pairs:", pairs)


tuple1 = (11, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print("\nAdded Tuple:", new_tuple)


print("Tuple Elements:")
for item in new_tuple:
    print(item)


num = int(input("\nEnter number to check in tuple: "))
if num in new_tuple:
    print(num, "is present in tuple")
else:
    print(num, "not present")


student = {
    "name": "Ratchita",
    "course": "AI",
    "marks": 95
}

print("\nDictionary Data:")
for key, value in student.items():
    print(key, ":", value)


value = int(input("\nEnter a value: "))

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Number is:", check(value))

if value < 5:
    print("Less than 5")
elif value == 10:
    print("Value is 10")
else:
    print("Greater than 5")


if value > 5:
    if value < 20:
        print("Value is between 5 and 20")
    else:
        print("Value is 20 or more")