# 2D Dimentional Dictionary
# Jika kita akan membuat sebuah dictionary dengan 
# menggunakan fungsi input() yang mana hasil dari
# inputan tersebut diletakkan pada setiap row yang ada
# pada dictionary, maka langkah awal kita akan 
# membuat varibael dictionary tanpa ada isinya
# terlebih dahulu, seperti contoh dibawah ini 
# dictionaryName = {}
# variabel "clue" adalah implementasi dari contoh
# diatas
""" clue = {}

# Code dibawah akan melakukan perulangan
# dimana kita akan diminta untuk mengsisi terus 
# 3 varibael masukan
while True:
    name = input("Name: ")
    location = input("Location: ")
    weapon = input("Weapon: ")
    # Pada code dibawah ini yang cukup menarik
    # karena disini kita akan membuat dictionary
    # berdasarkan row yang nantinya akan kita simpan 
    # pada variabel "clue"
    # dictNmae[Row Key Name] = {keyName: keyValue, NextkeyName: NextkeyValue}
    # implementasinya adalah code dibawah ini
    clue[name] = {"location": location, "weapon": weapon}
    # sehingga jika kita meminta outpunya adalah
    # dengan fungsi print dibawah
    print(clue)
    # {'Syarif': {'location': 'Yogyakarta', 'weapon': 'Windows'}, 
    # 'Arres': {'location': 'Jakarta', 'weapon': 'Mac'}} """

#=====================================================

# Jika sebelumnya hanya akan mencetak dalam bentuk
# dictionary biasa, bagaimana jika kita mempercantiknya
# dengan menambahkan subrutin
""" clue = {}

# Kode dibawah merupakan sebuah fungsi 
# yang disebut prettyPrint(). Fungsi ini 
# bertujuan untuk mencetak (print) isi dari 
# sebuah dictionary clue dengan format yang 
# lebih rapi dan mudah dibaca.

def prettyPrint():
    print()
    for key, value in clue.items():
        print(key, value)

# Code dibawah akan melakukan perulangan
# dimana kita akan diminta untuk mengsisi terus 
# 3 varibael masukan
while True:
    name = input("Name: ")
    location = input("Location: ")
    weapon = input("Weapon: ")
    # Pada code dibawah ini yang cukup menarik
    # karena disini kita akan membuat dictionary
    # berdasarkan row yang nantinya akan kita simpan 
    # pada variabel "clue"
    # dictNmae[Row Key Name] = {keyName: keyValue, NextkeyName: NextkeyValue}
    # implementasinya adalah code dibawah ini
    clue[name] = {"location": location, "weapon": weapon}
    # sehingga jika kita meminta outpunya adalah
    # dengan fungsi subrutin yang telah kita
    # buta sebelumnya
    prettyPrint()
    # maka haslinya akan tampak seperti dibawah ini
    # syarif {'location': 'Yogyakarta', 'weapon': 'Windows'}
    # Arres {'location': 'Jakarta', 'weapon': 'Mac'} """

#=====================================================

""" clue = {}

# Kode dibawah merupakan sebuah fungsi 
# yang disebut prettyPrint(). Fungsi ini 
# bertujuan untuk mencetak (print) isi dari 
# sebuah nested dictionary clue dengan format yang 
# lebih rapi dan mudah dibaca.

def prettyPrint():
    print()
    # Nested FOR
    for key, value in clue.items():
        print(key, end=": ")
        for subkey, subvalue in value.items():
            print(subkey, subvalue, end=" | ")
        print()

# Code dibawah akan melakukan perulangan
# dimana kita akan diminta untuk mengsisi terus 
# 3 varibael masukan
while True:
    name = input("Name: ")
    location = input("Location: ")
    weapon = input("Weapon: ")
    # Pada code dibawah ini yang cukup menarik
    # karena disini kita akan membuat dictionary
    # berdasarkan row yang nantinya akan kita simpan 
    # pada variabel "clue"
    # dictNmae[Row Key Name] = {keyName: keyValue, NextkeyName: NextkeyValue}
    # implementasinya adalah code dibawah ini
    clue[name] = {"location": location, "weapon": weapon}
    # sehingga jika kita meminta outpunya adalah
    # dengan fungsi subrutin yang telah kita
    # buta sebelumnya
    prettyPrint()
    # dan yang akan ditampilkan adalah seperti ini
    # syarif: location Yogyakarta | weapon Windows |
    # Arres: location Jakarta | weapon Mac | """

#=====================================================

# Simple Dictionary
""" jonh = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}
courseProgress = {"John": jonh, "Janet": janet, 
                  "Erica": erica}
# Code dibawah akan menampilkan seluruh dictionary yang ada
# pada variabel couseProgress
print(courseProgress)

# Code dibawah akan menampilkan dictionary yang ada pada
# couserProgress dengan key "Erica" saja
print(courseProgress["Erica"])

# Sedangkan code dibawah akan menampilkan dictionary
# yang ada pada variabel courseProgress dengan key
# "Ercica" untuk mencari value dari "daysCompleted"
# yang nantinya akan menampilkan angka 75, sesuai dengan
# data yang ada pada dictionary 
print(courseProgress["Erica"]["daysCompleted"]) """

#Project
import os, time

mokedex = {}

def prettyPrint():
  print(f"Name\tType\tHP\tMP")
  for key, value in mokedex.items():
    print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

while True:
  print("Add your Beast!")
  name = input("Name > ").title()
  type = input("Type > ").title()
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  mokedex[name] = { "type": type, "hp": hp, "mp": mp}
  print("----------")
  print()
  prettyPrint()
