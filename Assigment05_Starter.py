# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What): Achristnovich, 20220515, write data to txt file and load data from txt file.
# RRoot,1.1.2030,Created started script
# Anne Christnovich, 20220515, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFilename = "ToDoList.txt"   # An object that represents a file
lstRow = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open(objFilename, "r")
for row in objFile:
    try:
        lstRow = row.split(",") #splits on comma
        dicRow = {"task":lstRow[0], "prio":lstRow[1]} #key:value
        lstTable.append(dicRow) #adds data to memory
    except: #kept getting error when adding more data after hitting 4 once bc of extra new line characters.
        continue
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item. 
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [0 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        for dicRow in lstTable: #tells us what's in memory
            print(dicRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        #objFile = open(objFilename, "a")
        strTask = input("Enter a task: " + "\n")
        strPrio = input("Enter a priority of the task: " + "\n")
        dicRow = {"task": strTask, "prio": strPrio} #assigns key and value
        lstTable.append(dicRow) #adds to memory
        #objFile.write(lstRow[0] + "," + lstRow[1] + "\n")
        continue
    #Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        lstTable.pop() #removes last line of memory. I found pop() on google because I struggled to figure out a different solution.
        print("Last item on list deleted.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open(objFilename, "w") #overwites txt data so it doesn't write the same list multiple times.
        for row in lstTable:
            objFile.write(str(row["task"]) + "," + str(row["prio"] + "\n")) #unpack and assign as a string.
        objFile.close()
        print("Data saved and file closed.") 
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
