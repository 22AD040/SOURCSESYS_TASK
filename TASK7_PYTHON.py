# List with Multiple Data
my_list = [11, 2, 3, "ARTFICIAL INTELLIGENCE", 45.6]
print("Original List:", my_list)

#  Index and Slicing
print("First Element:", my_list[0])
print("Sliced List:", my_list[1:4])

#  For Loop
print("\nUsing For Loop:")
for item in my_list:
    print(item)

#  Append
my_list.append(100)
print("\nAfter Append:", my_list)

#  Remove, Pop, Delete
my_list.remove("ARTFICIAL INTELLIGENCE")
my_list.pop(1)
del my_list[0]
print("After Remove, Pop, Delete:", my_list)

#  Nested List
nested = [[1, 2], [3, 4], [5, 6]]
print("\nNested List:", nested)

for row in nested:
    for value in row:
        print("Nested Value:", value)

#  List Comprehension (Squares)
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print("\nSquares using List Comprehension:", squares)

#  Pairs using List Comprehension
pairs = [(x, y) for x in range(2) for y in range(2)]
print("Pairs:", pairs)

#  Tuple and Adding Tuples
tuple1 = (11, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print("\nAdded Tuple:", new_tuple)

#  Membership Concept
if 2 in new_tuple:
    print("2 is present in tuple")
else:
    print("2 not present")

#  If-Elif-Else
value = 10

if value < 5:
    print("Less than 5")
elif value == 10:
    print("Value is 10")
else:
    print("Greater than 5")

#  Nested If
if value > 5:
    if value < 20:
        print("Value is between 5 and 20")
