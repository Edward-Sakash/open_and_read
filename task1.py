# Step 1: Define the file path
file_path = "sample.txt"

try:
    # Step 2: Open the file in read mode
    with open(file_path, 'r') as file:
        # Step 3: Read and print the contents
        contents = file.read()
        print(contents)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

except IOError as e:
    print(f"Error: Unable to read the file '{file_path}': {e}")
