# Penggunaan modul "datetime"

import datetime

# Code dibawah akan menampilkan tahun, bulan 
# dan tanggal berdasarkan inputan pada value
# di dalam variabel "myData"
""" myDate = datetime.date(year = 2023, month = 12, day = 7)

print(myDate) """

#========================================

# Code dibawah akan menampilkan tahun, bulan
# dan tanggal setiap code dijalankan setiap
# harinya
""" today = datetime.date.today()
print(today) """

#========================================

# Membuat code inputan untuk tahun, bulan dan
# tanggal

""" year = int(input("Year: "))
month = int(input("Month: "))
days = int(input("Days: "))

date = datetime.date(year, month, days)

print(date) """

#========================================

# Code dibawah akan melakukan menyimpan value
# berdasarkan run code dari tahun, bulan dan hari
# dalam variabel "today"
""" today = datetime.date.today()
# Ini membuat objek timedelta yang mewakili selisih 
# waktu sebesar 3 hari. timedelta digunakan untuk 
# melakukan perhitungan waktu (seperti penambahan atau 
# pengurangan) pada objek tanggal.
difference = datetime.timedelta(days = 365)
# Ini melakukan penambahan tanggal saat ini (today) 
# dengan selisih waktu yang didefinisikan dalam "difference". 
# Hasilnya disimpan dalam variabel newDate.
newDate = today + difference
# Ini mencetak hasil penambahan tanggal baru (newDate).
print(newDate) """

#========================================

# Example menggunakan if - elif - else penggunaan datetime

today = datetime.date.today()

holiday = datetime.date(year = 2023, month = 8, day = 21)

if holiday > today:
    print("Coming Soon")
elif holiday < today:
    print("Hope You Enjoyed it!")
else:
    print("HOLDAY TIME!")

#========================================

# Project

# Kode di bawah digunakan untuk membuat 
# kalkulator hitungan mundur menuju sebuah 
# acara.

# Ini mengimpor modul datetime yang 
# memungkinkan kita untuk bekerja dengan 
# tanggal dan waktu di Python.
import datetime

print("🌟 Event Countdown Timer 🌟\n")

# Ini meminta pengguna untuk memasukkan 
# nama acara.
event = input("Input the event > ")
# Ini meminta pengguna untuk memasukkan 
# tahun acara.
year = int(input("Input the year > "))
#  Ini meminta pengguna untuk memasukkan 
# bulan acara.
month = int(input("Input the month > "))
# Ini meminta pengguna untuk memasukkan 
# tanggal acara.
days = int(input("Input the day > "))

# Ini mengambil tanggal saat ini dan 
# menyimpannya dalam variabel today.
today = datetime.date.today()

# Ini menggunakan input pengguna untuk 
# membuat objek tanggal yang mewakili 
# tanggal acara yang dimasukkan.
holiday = datetime.date(year, month, days)

# Ini menghitung selisih waktu antara 
# tanggal acara (holiday) dan tanggal 
# saat ini (today), dan menyimpannya 
# dalam variabel difference.
difference = holiday - today
# Karena difference adalah objek timedelta, 
# kita perlu mengakses atribut days untuk 
# mendapatkan selisih waktu dalam bentuk hari.
difference = difference.days

# Ini adalah kondisi jika selisih waktu 
# positif (artinya acara belum terjadi).
if difference > 0:
    print("Coming Soon!")
# Ini adalah kondisi jika selisih waktu 
# negatif (artinya acara telah berlalu).
elif difference < 0:
    print("Hope You enjoyed it!")
# Ini adalah kondisi jika selisih waktu 
# nol (artinya hari ini adalah tanggal acara).
else:
    print("Happy Birthday!!!")

# Ini mencetak selisih waktu dalam bentuk 
# jumlah hari.
print(difference)

# Hasil dari kode diatas akan menunjukkan 
# pesan berdasarkan selisih waktu antara 
# tanggal acara dan tanggal saat ini. 
# Jika selisih waktu positif, akan mencetak 
# "Coming Soon!". Jika selisih waktu negatif, 
# akan mencetak "Hope You enjoyed it!". 
# Jika selisih waktu nol, akan mencetak 
# "Happy Birthday!!!". Terakhir, kode ini 
# akan mencetak jumlah hari selisih waktu.