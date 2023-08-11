# Pada code dibawah akan membuatkan kita peniympanan
# 2D sementara pada RAM kita, jika menjalankan code
# Sehingga semua data yang dimasukkan bersifat
# menyimpan data sementara pada RAM PC
""" myEvents = []

# Subruitn dibawah ini akan menampilkan data
# yang mudah dibaca ketika kita selesai melakukan
# inputan
def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

# Perulangan dibawah akan meminta user untuk 
# memasukkan pilihan string antara 1 dan 2
while True:
  menu = input("1: Add, 2: Remove\n")
  # Jika kita memasukkan angka 1 maka perintah Add
  # akan dijalankan untuk menambahkan data
  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event,date]
    myEvents.append(row)
    prettyPrint()
  # Namun jika kita memasukkan angka selain 1, maka
  # perintah else akan dijalankan untuk menghapus
  # data yang ada pada list "myEvent[]"
  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row) """

#=================================================

# Code dibawah fungsinya sama seperti code diatas
# hanya saja yang membedakan adalah, jika code diatas
# membuat penyimpanan sementara pada RAM, code dibawah
# akan menyimpan data dengan membuat sebuah file baru
# yang akan menyimpan data yang telah diinput pada
# perulangan while dan statement if sehingga ketika
# program dihentikan data yang sebelumnya diinput,
# masih tetap ada pada file

# Awalnya kita akan menyimpan data pada variabel
# dibawah ini "myEvent[]"
""" myEvents = []

def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

while True:
  menu = input("1: Add, 2: Remove\n")

  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event,date]
    myEvents.append(row)
    prettyPrint()

  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row)
        
  # Setelah data yang dimasukkan pada variabel
  # "myEvent[]" maka selanjutnya akan dibuatkan
  # file baru dengan nama "calender.txt" dengan
  # perintah "w" (write) untuk membuat file
  # ketika file telah terbuat maka langkah selanjutnya
  # adalah mentransmisikan (mengirimkan) data yang
  # ada pada variabel "myEvent[]" dalam bentuk string
  # yang akan disimpan pada file "calender.txt"
  ########### THIS IS THE NEW BIT ########
  f = open("calendar.txt", "w") # Permissions set to 'w' because we are deleting the file and replacing it with the whole 2D list every time.
  f.write(str(myEvents)) # Need to cast the list to a single string
  f.close()
  ######################################### """
  
#==================================================

# Pada code sebelumnya kita telah membuat penyimpanan
# pada data yang telah kita masukkan, untuk selanjutnya
# kita akan menggunakan fungsi "eval(code string)" 
# agar setiap kita menambahkan data, jika program
# sebelumnya kita telah memasukkan data maka jika
# kita menjalankannya kembali data yang sudah ada
# sebelumnya tidak tergantikan dengan data baru, 
# namun akan menambahkan data pada list dengan
# berbeda index-nya
myEvents = []

####### THIS IS THE NEW BIT ################
f=open("calendar.txt","r") # Only need read permissions here
# Fungsi eval(code string) menjalankan kode 
# dalam tanda kurung dan mengembalikan kode kerja
# String kode adalah teks apa pun yang 
# benar-benar hanya kode
myEvents = eval(f.read())
f.close()
########################################

def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

while True:
  menu = input("1: Add, 2: Remove\n")

  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event,date]
    myEvents.append(row)
    prettyPrint()

  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row)

  
  f = open("calendar.txt", "w") 
  f.write(str(myEvents)) 
  f.close()

# Project
# Buatlah seperti code pada days 45