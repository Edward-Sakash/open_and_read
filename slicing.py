"""
    (Slicing)
Given the following list, use slicing to extract the specified portions:
```python
# Exercise list
exercise_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
1. Extract the first three elements of the list.
2. Extract the elements from index 4 to index 7 (inclusive).
3. Extract every second element from the list.
4. Extract the last four elements of the list.
5. Reverse the list using slicing.

"""

# Solution
# Exercise list
exercise_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Extract the first three elements of the list.
first_three_elements = exercise_list[:3]
print(first_three_elements)  # Output: [1, 2, 3]

# 2. Extract the elements from index 4 to index 7 (inclusive).
elements_from_4_to_7 = exercise_list[4:8]
print(elements_from_4_to_7)  # Output: [5, 6, 7, 8]

# 3. Extract every second element from the list.
every_second_element = exercise_list[::2]
print(every_second_element)  # Output: [1, 3, 5, 7, 9]

# 4. Extract the last four elements of the list.
last_four_elements = exercise_list[-4:]
print(last_four_elements)  # Output: [7, 8, 9, 10]

# 5. Reverse the list using slicing.
reversed_list = exercise_list[::-1]
print(reversed_list)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


