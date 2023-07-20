import json

# Step 1: Define the file path
file_path = "data.json"

try:
    # Step 2: Open the JSON file and load its content as a dictionary
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Step 3: Extract the employee information from the dictionary
    employees = data["employees"]

    # Step 4: Print the employee details
    for employee in employees:
        name = employee["name"]
        age = employee["age"]
        department = employee["department"]
        print(f"Name: {name}, Age: {age}, Department: {department}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

except json.JSONDecodeError as e:
    print(f"Error: Unable to parse the JSON content from the file '{file_path}': {e}")

except IOError as e:
    print(f"Error: Unable to read the file '{file_path}': {e}")
