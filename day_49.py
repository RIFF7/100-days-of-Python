# Cara membuka file yang ada pada folder
# f = open(file name, mode)
# f = adalah variabel yang dibuat
# open() = adalah fungsi yang digunakan untuk membaca file
# file name = adalah nama file sesuai yang ada pada folder
# mode = adalah perintah untuk menjalankan sebuah file
# dari membaca (r), menulis (w) dan lainnya

# Example 1
# Code dibawah akan membaca file dengan nama
# filenames.list
""" f = open("filenames.list", "r")
f = open("filenames.list", "r")
contents = f.read()
f.close()

print(contents) """

# Example 2
# Code dibawah akan membaca file dengan nama filenames.list
# dan menjadikannya sebagai list dengan fungsi split()
# sehingga akan menampilkan data menjadi elemen pada
# sebuah list
""" f = open("filenames.list", "r")
contents = f.read()
f.close()

contents = contents.split() #added split here

print(contents) """

# Example 3
# Code dibawah akan membaca data pada file
# filenames.list secara individual
""" f = open("filenames.list", "r")
content = f.readline()
print(content)

f.close() """

# Example 4
# Code dibawah akan membaca data yang ada pada file
# filenames.list satu per satu dengan menghilangkan
# spasi berlebih ketika terdapat pada data dengan
# menggunakan fungsi strip()
""" f = open("filenames.list","r")
contents = f.readline().strip()
print(contents)
contents = f.readline().strip()
print(contents)
contents = f.readline().strip()
print(contents)
contents = f.readline().strip()
print(contents)

f.close() """

# Example 5
# Code dibawah akan membaca data yang ada pada file
# filenames.list satu per satu dengan menghilangkan
# spasi berlebih ketika terdapat pada data dengan
# menggunakan fungsi strip()
""" f = open("filenames.list","r")
# Code dibawah akan digunakan untuk mengulang
# membaca data dari filenames. list
while True:
  contents = f.readline().strip()
  
  # Jika baris terakhir dalam file kosong maka
  # perintah if akan dijalankan 
  if contents == "":
    break
  # Dan ketika memang baris data yang dibaca selanjutnya
  # bernilai kosong maka program akan dihentikan dengan
  # fungsi "break"

  # Code dibawah memindahkan cetakan setelah jeda 
  # sehingga tidak menampilkan baris kosong terakhir.
  print(contents)

f.close() """

# Project
import os, time

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("The winner is", name, "with", highscore)