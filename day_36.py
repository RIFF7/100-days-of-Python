#Example 1 -> ketika kita menginput tulisan david 
#tidak sesuai rule maka else akan dijalankan

""" name = input("What's your name? ")
if name == "David" or name == "David":
    print("Hello Baldy!")
else:
    print("What a beatiful head of hair!") """

#Example 2 -> ketika kita menginput tulisan david
#tidak sesuai aturan maka perintah lower akan dijalankan 
#mengubahnya menjadi huruf kecil, sehingga nilainya
#sama dengan rule yang ada

""" name = input("What's your name? ")
if name.lower() == "david":
    print("Hello Baldy!")
else:
    print("What a beatiful head of hair!") """

#Example 3 -> ketika kita menginput kata david 
#menggunakan spasi diawal maka perintah strip akan 
#menghilangkan spasi sebelum awal tulisan

""" name = input("What's your name? ")
if name.lower().strip() == "david":
    print("Hello Baldy!")
else:
    print("What a beatiful head of hair!") """

#Example 4
""" myList = []

def printList():
    print()
    for i in myList:
        print(i)
    print()

#Perintah capitalize() dan strip() ini 
#akan merubah inputan huruf pertama 
#menjadi huruf besar dan menghilangkan spasi 
#ketika pas input kita tidak / sengaja diawal
#menekan spasi dan jika data yang kita masukkan
#bernilai sama maka data tersebut tidak ada dimasukkan

while True:
    addItem = input("Item > ").strip().capitalize()
    if addItem not in myList:
        myList.append(addItem)
    printList() """

#Project 1
rolodex = []

def printList():
  print()
  for name in rolodex:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in rolodex:
    rolodex.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()