""" \n -> New Line
\t -> Tab
\v -> Vertical Tab"""

#Example penggunaan end
""" for i in range(0, 100):
    print(i) """
    
""" for i in range(0, 100):
    print(i, end="") """

""" for i in range(0, 100):
    print(i, end=" ") """

""" for i in range(0, 100):
    print(i, end=", ") """

""" for i in range(0, 100):
    print(i, end="\n") """

""" for i in range(0, 100):
    print(i, end="\t") """

""" for i in range(0, 100):
    print(i, end="\v") """

""" Saya dapat menghidupkan dan mematikan 
warna pada bit kode yang berbeda dengan 
menggunakan end. Hapus kode sebelumnya dari 
file main.py Anda dan coba ini. """
    
""" print("If you put")
print("\033[33m", end="") #yellow
print("nothing as the")
print("\033[35m", end="") #purple
print("end character")
print("\033[32m", end="") #green
print("then you don't")
print("\033[0m", end="") #default
print("get odd gaps") """

""" print("If you put", "\033[33m", 
"nothing as the", "\033[35m", "end character", 
"\033[32m", "then you don't", 
"\033[0m", "get odd gaps", end="") """

""" Ambil kode yang sama ini dan ubah ujung 
ke sep (kependekan dari pemisah) dan tambahkan 
spasi di akhir setiap string. Apa yang terjadi?
ini akan menghilangkan white space pada text"""

""" print("If you put ", "\033[33m", 
"nothing as the ", "\033[35m", 
"end character ", "\033[32m", 
"then you don't ", "\033[0m", 
"get odd gaps ", sep="") """

#Menampilkan iterasi tanpa perintah kecepatan (default)
""" import os

for i in range(1, 101):
  print(i)
  os.system("cls") """
  
#Menampilkan iterasi dengan kecepatan 0.5
""" import os, time

for i in range(1, 101):
  print(i)
  time.sleep(0.5)
  os.system("cls") """

#Menampilkan iterasi dengan kecepatan 0.01
""" import os, time

for i in range(1, 101):
  print(i)
  time.sleep(0.01)
  os.system("cls") """

#Mematikan kursor saat memulai iterasi dengan perintah print('\033[?25l', end="")
""" import os, time
print('\033[?25l', end="")
for i in range(1, 101):
  print(i)
  time.sleep(0.2)
  os.system("cls") """

#Mengaktifkan kembali kursor dengan perintah print('\033[?25h', end="")
""" import os, time
print('\033[?25h', end="")
for i in range(1, 101):
  print(i)
  time.sleep(0.2)
  os.system("cls") """


""" ada kode yang diberikan, end="" 
digunakan untuk mengontrol karakter yang 
dicetak setelah baris teks selesai diproses 
oleh fungsi print(). Secara default, 
setelah mencetak baris teks, fungsi print() 
akan menambahkan karakter newline ("\n") 
pada akhir baris, sehingga mencetak baris 
baru dan berpindah ke baris berikutnya. 
Namun, dengan menggunakan end="", 
karakter newline tidak akan ditambahkan, 
sehingga baris berikutnya akan dicetak 
di samping baris sebelumnya. """

def newPrint(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print("With my ", end="")
newPrint("red", "new program")
newPrint("reset", " I can just call red('and') ")
newPrint("red", "it will print in red ")
newPrint("blue", "or even blue")
