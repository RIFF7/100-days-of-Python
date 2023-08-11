import os, time, random
# Subrutin dibawah digunakan untuk membuat file dan 
# menambahkan data pada file yang telah dibuat dengan
# fungsi "w" (write) untuk membuat file dan "a+" untuk
# menambah data dalam file dan membaca file
def add():
  os.system("clear")
  idea = input("Idea > ")
  f = open("creat.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  time.sleep(1)
  os.system("clear")
  
# Subrutin dibawah ini digunakan untuk membaca
# data dengan fungsi "r" (read) dan menampilkannya
# secara acak menggunakan funsgi 
# random.choice(variabel)
def show():
  os.system("clear")
  f = open("creat.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  time.sleep(2)
  os.system("clear")

# Perulangan dibawah akan meminta user untuk
# memasukan pilihan antara tambah data atau 
# tampilkan data secara acak
while True:
  menu = input("1: Add idea\n2: Show a random idea\n> ")
  # Jika user memilih option 1, maka perintah
  # dari subrutin add() akan dijalankan
  if menu == "1":
    add()
  # Namun jika user memasukan string selain 1,
  # maka perintah subrutin dari show() akan
  # dijalankan
  else:
    show()