import os, time, random
# Pertama kita akan membuat variabel "trumps"
# untuk menampung isi dalam dictionary yang 
# akan dibuat 
trumps = {}
# Code dibawah adalah key dan sub keys serta value
# yang telah dibuat dan akan ditampung pada variabel
# "trumps"
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}
# Dibawah adalah perulangan while, yang akan digunakan
# untuk menanyakan pada player / user untuk memilih
# character yang ada dalam dictionary "trumps"
while True:
  print("TOP TRUMPS")
  print()
  print("Characters")
  print()
    # Perulangan dibawah akan menampilkan isi dalam
    # keys dictionary yang ada pada variabel "trumps"
  for key in trumps:
    print(key)
    # Setelah perulangan tercapai maka player / user
    # akan diminta untuk memilih karakter yang ada
    # dalam dictionary pada variabel "trumps"
  user = input("Pick your character\n> ")
    # Setelah user / player selesai memilih
    # maka selanjutnya giliran komputer yang akan 
    # memilih, namun disini pilihan komputer akan
    # ditentukan secara random berdasarkan keys list
    # yang ada pada dictionary "trumps"
  comp = random.choice(list(trumps.keys()))
  print("Computer has picked", comp)

  print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")
    # Lalu setelah user dan komputer selesai memilih
    # maka selanjutnya code dibawah akan dijalankan
    # untuk meminta user / player memilih 
    # sub key berdasarkan data 
    # dalam dictionary "trumps"
  answer = input("> ")
    # Setelah sub key selesai dipilih maka code
    # dibawah akan dijalankan untuk menampilkan
    # hasil pilihan yang dimasukkan sebelumnya
    # yaitu sub key, sehingga jika user / player
    # memilih salah satu data sub key yang ada
    # dalam dictionary "trumps" maka setelah itu 
    # akan menampilkan data dari key, sub key dan 
    # value yang ada dalam dictionary "trumps"
  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp}: {trumps[comp][answer]}")
    # Code dibawah akan melakukan pengecekan pada
    # key, sub key dan value dari dictionary
    # jika key dan sub key dari user / player
    # lebih besar valuenya, maka perintah "if"
    # akan dijalankan, namun 
    # jika key dan sub key dari komputer lebih
    # besar valuenya, maka perintah "elif" akan
    # dijalankan dan ketika valuenya sama, maka
    # code dari "else" akan dijalankan
  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")
    # code dibawah untuk menjeda tampilan hasil
    # dari resul pengecekan statement if - elif
  time.sleep(2)
    # code dibawah akan melakukan pembersihan 
    # tampilan, agar kembali ke tampilan awal
    # dari perulangan while lagi
  os.system("clear")