import sys

# Init
file_name = "todo_data.txt"
todos = []

# Read File
try:
    file = open(file_name, "r")
    todos = file.readlines()
    file.close()
except:
    pass

print(todos)

# Add

# Remove Todo

# Save File
try:
    file = open(file_name, "w")
    file.writelines(todos)
    file.close()
except:
    pass

# Print List

# Print Commands
print("\n**********************************\n")
print(f"View ToDos:")
print(f"Add ToDo:")
print(f"Remove or Complete ToDo:")
print("\n**********************************\n")