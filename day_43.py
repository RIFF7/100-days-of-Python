""" Cara membuat sebuah tabel menggunakan list
    Example:
    - listName[row index][column index]
    - listName[[first list], [second list]]
    
    my2Dlist[2][1] dari perintah ini keluarannya
    untuk tabel dibawah adalah?
    
    Example of Table:
    
        0       1       2
    0 Jonh      21      Mac
    1 David     128     Babbage
    2 Sian      32      Mac
    3 Katie     38      IBM 386
    4 Daisy     44      Amiga
    
    Jadi ketika kita membuat list
    
    myList[2][1]
    
    yang akan ditampilkan adalah pada row ke-2
    dan kolom pertama yaitu 32
    
    Example 2:
    - listName[row index][column index] = value
    perintah diatas digunkan untuk merubah value
    yang sebelumnya ada pada list awal
"""

myList = [["John", 17, "Mac"],
          ["Angel", 19, "Linux"],
          "Roki", 25, "Windows"]

#Menampilkan isi keseluruhan pada list
print(myList)

#Menampilkan spesifik list dengan index
print(myList[0][0])

#Merubah isi pada list awal
myList[1][2] = "Apple"

print(myList[1])

#Project
""" Kita akan membuat sebuah tabel dengan list
    bernama myNansBingoCard yang isinya adalah:
    
        0       1       2   #Ini adalah kolom
    0  10      22      31
    1  41     BINGO    73   #ini adalah rows
    2  84      88      89
"""
import random

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

prettyPrint()

""" Kode di atas merupakan implementasi sederhana 
dari permainan bingo dengan kartu bingo berukuran 
3x3.

Fungsi num():
Fungsi ini digunakan untuk menghasilkan 
angka acak antara 0 hingga 90 (inklusif). 
Setiap kali fungsi ini dipanggil, 
akan mengembalikan angka acak baru.

Fungsi prettyBingo():
Fungsi ini digunakan untuk mencetak kartu 
bingo dengan tata letak yang lebih rapi. 
Kartu bingo yang telah dibentuk dalam bentuk 
list bingo akan dicetak menggunakan fungsi ini.

Generate Angka Acak untuk Kartu Bingo:
Pada bagian ini, kode akan menghasilkan 10 
angka acak dengan memanggil fungsi num() 
sebanyak 10 kali, dan hasilnya akan disimpan 
dalam list numbers. Setelah itu, angka-angka 
dalam list numbers akan diurutkan.

Membentuk Kartu Bingo:
Kartu bingo berukuran 3x3 akan dibentuk 
dengan mengisi list bingo. Di sini, 
kita hanya menggunakan beberapa angka acak 
dari list numbers untuk mengisi kartu bingo 
dengan format sebagai berikut:

numbers = [num1, num2, num3, num4, num5, 
            num6, num7, num8, num9, num10]

bingo = [[num1, num2, num3],
         [num4, "BINGO", num5],
         [num6, num7, num8]]

Kode menggunakan angka acak dari numbers 
untuk mengisi posisi yang ditentukan 
dalam kartu bingo. Posisi tengah kartu bingo 
ditandai dengan "BINGO". 
Angka acak yang dipilih dan ditempatkan 
dalam kartu bingo ini akan berbeda setiap 
kali kode dieksekusi karena mereka berasal 
dari angka acak yang dihasilkan oleh num().

Mencetak Kartu Bingo:
Setelah kartu bingo selesai dibentuk, 
fungsi prettyBingo() dipanggil untuk mencetak 
kartu bingo dengan tata letak yang lebih rapi. 
Kartu bingo akan dicetak dalam format 3x3 
dan angka acak serta "BINGO" yang berada 
dalam kartu bingo akan ditampilkan.

Kode ini hanya menghasilkan satu kartu bingo 
dengan angka acak, tetapi Anda dapat mengubahnya 
untuk menghasilkan lebih banyak kartu bingo 
dengan memodifikasi jumlah angka acak yang 
dihasilkan dan memperbarui kartu bingo dengan 
cara yang sesuai.

Sedangkan kegunaan code dibawah:

numbers = []
for i in range(10):
    numbers.append(num())
    
membuat list numbers yang berisi 10 angka acak.
Proses tersebut dijalankan dengan melakukan 
iterasi menggunakan for loop dengan i sebagai 
variabel iterasi. Loop ini akan berjalan sebanyak 
10 kali karena range(10) menghasilkan urutan 
angka dari 0 hingga 9.

Pada setiap iterasi, code num() dipanggil 
untuk menghasilkan angka acak antara 0 hingga 90 
(inklusif). Angka acak tersebut kemudian 
ditambahkan ke dalam list numbers menggunakan 
metode append().

Akhirnya, setelah loop selesai berjalan, 
list numbers akan berisi 10 angka acak 
yang dihasilkan dari fungsi num().
"""