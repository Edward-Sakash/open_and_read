# Step 1: Define the file paths
input_file_path = "input.txt"
output_file_path = "reversed.txt"

try:
    # Step 2: Open the input file in read mode
    with open(input_file_path, 'r') as input_file:
        # Step 3: Read the content of the input file
        content = input_file.read()

        # Step 4: Reverse the content
        reversed_content = content[::-1]

    # Step 5: Open the output file in write mode
    with open(output_file_path, 'w') as output_file:
        # Step 6: Write the reversed content to the output file
        output_file.write(reversed_content)

    print(f"Content of '{input_file_path}' was reversed and written to '{output_file_path}' successfully.")

except FileNotFoundError:
    print(f"Error: The file '{input_file_path}' was not found.")

except IOError as e:
    print(f"Error: Unable to read or write files: {e}")
