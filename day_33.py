#Chalange
#Penggun list untuk menambah dan menghapus
""" mylist = []

def prinList():
    print()
    for item in mylist:
        print(item)
    print()

while True:
    
    menu = input("Add or Remove? ")
    
    if menu == "add" or menu == "Add":
        item = input("What's next Agenda in list? ")
        mylist.append(item)    
    elif menu == "remove" or menu == "Remove":
        
        item = input("What do you want to remove? ")
        
        if item in mylist:
            mylist.remove(item)
        else:
            print()
            print(f"{item}, was not in the list!")
        
    prinList() """


#Next Chalange
import os, time
toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif menu=="edit":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)