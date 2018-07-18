def printCommands():
    print("Congratulations! You're running Ryan's Task list program.")
    print("What would you like to do next?")
    print("1. List all tasks.")
    print("2. Add a task to the list.")
    print("3. Delete a task.")
    print("q. To quit the program")

printCommands()

aTaskListArray = ["bob", "dave"]

userSelection = input('Enter a command: ')

if userSelection == "1":
    for itemList in aTaskListArray:
        print(itemList)
    userSelection = input('Enter a command: ')

if userSelection == "2":
    newTask = input("What would you like to add? ")
    aTaskListArray.append(newTask)
    userSelection = input("Enter a command: ")

if userSelection == "3":
    newTask = input("What would you like to remove? ")
    aTaskListArray.remove(newTask)
    userSelection = input("Enter a command: ")


if userSelection == "q":
    quit()

else:
    print("Not a command")

print(aTaskListArray)