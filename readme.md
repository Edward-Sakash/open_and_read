# Exercise 1 (open1):
Write a Python program that opens a file called "sample.txt" and prints its contents.

# Exercise 2 (open2):
Write a Python program that opens a file called "numbers.txt", reads two integers from the file, and prints their sum.
Assume that the file "numbers.txt" contains two integers separated by a space, e.g., "10 20". (edited) 

# Exercise 3 (write 1):
Write a Python program that creates a new file called "output.txt" and writes the numbers 1 to 10, each on a new line.

# Exercise 4 (read and write):
Write a Python program that reads the content of a file called "input.txt" and writes the reversed content to a new file called "reversed.txt".

# Bonus (json):
Write a Python program that reads a JSON file called "data.json" and converts its contents into a dictionary.
The "data.json" file contains information about employees in a company.
Each employee has a name, age, and department.
data.json:
{
    "employees": [
        {
            "name": "John Doe",
            "age": 30,
            "department": "Engineering"
        },
        {
            "name": "Jane Smith",
            "age": 25,
            "department": "Marketing"
        },
        {
            "name": "Mike Johnson",
            "age": 35,
            "department": "Sales"
        }
    ]
}
Hint:
research about json
research the json module

# Bonus 2 (Slicing)
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


# Bonus 3 (Unpacking)
Given the following tuple, use unpacking to assign the elements to individual variables:
Assign each element to separate variables `a`, `b`, `c`, `d`, and `e`.
# Print the variables
print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30
print(d)  # Output: 40
print(e)  # Output: 50

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