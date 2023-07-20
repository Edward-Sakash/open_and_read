# Step 1: Define the file path
file_path = "output.txt"

try:
    # Step 2: Open the file in write mode
    with open(file_path, 'w') as file:
        # Step 3: Write the numbers 1 to 10 to the file
        for number in range(1, 11):
            file.write(str(number) + '\n')

    print(f"The numbers 1 to 10 were written to '{file_path}' successfully.")

except IOError as e:
    print(f"Error: Unable to write to the file '{file_path}': {e}")
