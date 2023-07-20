"""
# Bonus 4 (Nested Unpacking)
Given the following nested list, use unpacking to assign the elements to individual variables.

# Exercise nested list
nested_list = [1, 2, [3, 4, 5], 6, [7, 8], 9, 10]
1. Assign the first element to variable `a`, the second element to variable `b`, and the last element to variable `c`.
2. Assign the first three elements inside the inner list to variables `x`, `y`, and `z`.
# 1. Assign the first element to variable a, the second element to variable b, and the last element to variable c.
# 2. Assign the first three elements inside the inner list to variables x, y, and z.
# Print the variables
print("a:", a)  # Output: 1
print("b:", b)  # Output: 2
print("c:", c)  # Output: 10
print("x:", x)  # Output: 3
print("y:", y)  # Output: 4
print("z:", z)  # Output: 5

"""

# Solution

# Exercise nested list
nested_list = [1, 2, [3, 4, 5], 6, [7, 8], 9, 10]

# 1. Assign the first element to variable `a`, the second element to variable `b`, and the last element to variable `c`.
a, b, *_, c = nested_list

# 2. Assign the first three elements inside the inner list to variables `x`, `y`, and `z`.
_, _, [x, y, z], *_ = nested_list

# Print the variables
print("a:", a)  # Output: 1
print("b:", b)  # Output: 2
print("c:", c)  # Output: 10
print("x:", x)  # Output: 3
print("y:", y)  # Output: 4
print("z:", z)  # Output: 5
