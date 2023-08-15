# Read data from "csv" file
# "csv" file adalah bentukan data yang terdiri dari
# comma (koma), separated (terpisah), value (nilai)
# Example open "csv" file:
""" with open(File Name) as file:
        reader = csv.reader(file)
        for row in reader:
            do something to each row"""
# File Name = opens the csv file so it can be
# manipulated as if it were a list

# do something to each row = or rather, a 2D list
# that's why we need the loop

# Example in real code
#import csv

""" with open("January.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row) # Menampilkan data yang ada pada file csv dalam bentuk list
        print(", ".join(row)) # Menampilkan data bukan dalam bentuk list dan dapat dibaca serta menambahkan koma
        #print("\t".join(row)) # Menampilkan data dalam bentuk yang bisa dibaca dengan penambahan tab """

""" with open("January.csv") as file: 
  reader = csv.DictReader(file) # Treats the file as a dictionary 
  #line = 0
  total = 0.0
  for row in reader: 
    print (row["Net Total"])
    total += float(row["Net Total"])

print(f"Total: {total}") """

# Project
# Menghitung total biaya pada file csv "Day54Totals.csv"
import csv

# Code dibawah akan memulai nilai total dengan 0.0
total = 0.0

# Pada code dibawah akan membuka file csv
# "Day54Totals.csv" dengan alias "file"
with open("Day54Totals.csv") as file:
    # Code dibawah adalah cara untuk membuat 
    # objek pembaca yang akan membaca isi file 
    # CSV yang disebut file dalam mode berbasis 
    # kamus. Ini berarti bahwa setiap baris dalam 
    # file CSV akan dibaca sebagai sebuah kamus 
    # (dictionary) di mana kunci-kunci kamusnya 
    # adalah nama kolom di file CSV, dan 
    # nilai-nilai kamusnya adalah nilai-nilai dari 
    # kolom tersebut.
    reader = csv.DictReader(file)
    # Code dibawah akan melakukan iterasi
    # sebanyak data yang ada
    for row in reader:
        # Pada code dibawah setiap kali kita membaca 
        # baris dari file CSV, kita langsung 
        # menghitung total biaya dengan mengalikan 
        # quantity dan cost dari baris tersebut dan 
        # menambahkannya ke total keseluruhan. 
        # Dengan kata lain, kita melakukan penambahan 
        # langsung ke total pada setiap iterasi loop, 
        # sehingga total akhir akan mencerminkan 
        # jumlah total biaya dari seluruh baris dalam 
        # file.
        total += float(row["Quantity"]) * float(row["Cost"])
# Setelah selesai melakukan iterasi dan menghitung 
# total maka akan di cetak dengan code dibawah
# fungsi round adalah mengambil pembulatan 
# angka total yang dicetak ke dalam format uang 
# (dalam hal ini, format dolar) menjadi dua 
# tempat desimal setelah titik desimal.
print(f"Total: ${round(total, 2)}")