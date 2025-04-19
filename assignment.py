# read a file and write to a file
# Open the file in read mode
with open("assignment.txt", "r") as file:
  content = file.read()
  print(content)  # Print the content of the file


# writing to a file
with open("sample.txt", "w") as file: 
    file.write("Hello, World!")  # Write to the file
    file.write("\nThis is a new line.")  # Write another line to the file
    file.write("\nThis is a new line.")  # Write another line to the file
    file.write("\nThis is a new line.")
    file.write("\nThis is a new line.") 

# handling errors    
try:
    with open("inaccessible.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found. Please check the filename.")