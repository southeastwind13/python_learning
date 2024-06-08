'''
List Comprehension

List comprehension is a way to create lists based on existing lists.
It is a compact way to create new lists based on existing ones.

syntax:
1. Case if
new_list = [new_item for item in list if test == True]

2. Case if-else
new_list = [new_item if test == True else new_item2 for item in list ]

'''

numbers = [1, 2, 3, 4]
new_list1 = [n + 1 if n % 2 == 0 else 0 for n in numbers]
new_list2 = [n + 1 for n in numbers if n % 2 == 0 ]

print(new_list1) # [0, 3, 0, 5]
print(new_list2) # [3, 5]