# Cara membuka file yang ada pada folder
# f = open(file name, mode)
# f = adalah variabel yang dibuat
# open() = adalah fungsi yang digunakan untuk membaca file
# file name = adalah nama file sesuai yang ada pada folder
# mode = adalah perintah untuk menjalankan sebuah file
# dari membaca (r), menulis (w) dan lainnya

# Example 1
# Code dibawah akan melakukan perintah pembuatan file
# dengan fungsi "w" atau write
""" f = open("days_48.txt", "w")
# Code dibawah ini akan menuliskan kata yang ada pada
# file yang telah kita buat dengan nama 
# days_48.txt
f.write("Hello there!") 
# Setelah kata ditambahkan maka code dibawah akan
# dijalankan untuk mengakhiri program
f.close() """

# Example 2
# Selanjutnya kita akan membuat sebuah text dengan
# inputan
# Code dibawah akan melakukan perintah pembuatan file
# dengan fungsi "w" atau write
""" f = open("days_48.txt", "w")
whatText = input("> ")
# Code dibawah akan mencetak sebuah tulisan dari
# varibael whatText yang kita input
f.write(whatText)
# Setelah kata ditambahkan maka code dibawah akan
# dijalankan untuk mengakhiri program
f.close() """

# Example 3
# Code dibawah akan melakukan perintah penambahan kata
# dengan fungsi "a+"
""" f = open("days_48.txt", "a+")
whatText = input("> ")
# Code dibawah akan mencetak kata tambahan yang diinput
# sebelumnya dengan setiap kata baru akan muncul
# pada baris baru dengan perintah \n menggunakan
# f-string
f.write(f"{whatText}\n")
# Setelah kata ditambahkan maka code dibawah akan
# dijalankan untuk mengakhiri program
f.close() """

# Project
import os, time

while True:
  print("HIGH SCORE TABLE")
  print()
  name = input("INITIALS > ").upper()
  score = input("SCORE > ")
  print()

  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("ADDED")
  time.sleep(1)
  os.system("cls")