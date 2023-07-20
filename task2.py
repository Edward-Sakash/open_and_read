# Step 1: Define the file path
file_path = "numbers.txt"

try:
    # Step 2: Open the file in read mode
    with open(file_path, 'r') as file:
        # Step 3: Read the contents and split the numbers
        contents = file.read()
        numbers = contents.split()

        # Step 4: Convert the numbers to integers and calculate the sum
        if len(numbers) >= 2:
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            sum_of_numbers = num1 + num2
            print(f"The sum of {num1} and {num2} is: {sum_of_numbers}")
        else:
            print("Error: The file does not contain two integers separated by a space.")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

except ValueError:
    print("Error: The file does not contain valid integers.")

except IOError as e:
    print(f"Error: Unable to read the file '{file_path}': {e}")
