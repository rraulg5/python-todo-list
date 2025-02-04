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

# Add
if len(sys.argv) >= 3 and sys.argv[1].lower() == "add":
    todos.append(f"{sys.argv[2]}\n")

# Remove Todo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "remove":
    try:
        index_delete = int(sys.argv[2])
        if index_delete > 0:
            del(todos[index_delete - 1])
        else:
            print("Wrong number")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

# Save File
try:
    file = open(file_name, "w")
    file.writelines(todos)
    file.close()
except:
    pass

# Print List
if len(todos) == 0:
    print("You have no ToDos :)")
else:
    print("\nHere's your ToDo list:\n")
    for i in range(len(todos)):
        print(f"{i + 1}. {todos[i]}", end = "")

# Print Commands
print("\n**********************************")
print("COMMANDS")
print("---")
print(f"To View ToDos:\n{sys.argv[0]}")
print("---")
print(f"To Add a ToDo:\n{sys.argv[0]} add \"Something to do...\"")
print("---")
print(f"To Remove or Complete ToDo:\n{sys.argv[0]} remove [Number]")
print("**********************************\n")