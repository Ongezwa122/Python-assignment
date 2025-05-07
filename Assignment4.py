# Question 1: file handling

        # Open the file in read mode
try:
    with open("file4.txt", "r") as file:
        content = file.read()
        print(content)


      # Modify the content
        modified_content = content.upper()
        print(modified_content)

        # Open the file in write mode to overwrite the content
    with open("file4.txt", "w") as file:
        file.write(modified_content)
        print("File content modified successfully.")
except FileNotFoundError:
        print("File not found. Please check the filename.") 

# Question 2:
file4 = input("file4.txt")
try:
    with open("file4.txt", "r") as file:
       content = file.read()
  # Modify the content (example: replace "hello" with "hi")
       modified_content = content.lower()
       print(modified_content)

    # Save to a new file
       file4 = "modified_content" + file4
    with open(file4, "w") as file4:
        file4.write(modified_content)

        print(f"Modified content has been saved to '{file4}'.")

except FileNotFoundError:
       print(f"Error: File '{file4.txt}' not found.")
except IOError:
       print(f"Error: Could not read the file '{file4}'.")   
       print("Original content:\n", content)






