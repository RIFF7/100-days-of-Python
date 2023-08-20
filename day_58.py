# Pada Days 58 ini kita akan mengulik tentang
# penggunaan Run and Debug code pada python

# Example 1 Debug dengan klik baris ke 8 sampai
# tanda sircle warna merah (Breakpoints) muncul, lalu jalankan
# code program dengan memilih "Debug Python File"
""" for i in range(5):
    print(i) """
    
#============================================

# Example 2
""" import random

colors = ["Red", "Orange", "Yellow", "Green",
          "Teal", "Blue", "Purple", "Violet"]

while True:
    menu = input("1. Color\n2. Exit\n> ")
    if menu == "1":
        print(random.choice(colors))
    else:
        break """

#=============================================

# Project Breakpoints
# Pada code dibawah kita akan menjalankannya
# menggunakan Debug file dengan menggunakan 
# Breakpoint, sehingga kita akan mengetahui 
# letak kesalah code terdapat dimana, dengan
# klik baris code Breakpoint, jika angka
# pada variabel "number" berubah, maka terdapat
# kesalahan pada code, namun jika tidak maka
# code sudah sesuai
import random

totalAttempts = 0

def game ():
    attempts = 0
    # Dibawah adalah code yang sesuai, dimana
    # ketika program dijalankan value dari
    # "number" tidak berubah hanya 1 kali
    # muncul setiap program dijalankan
    number = random.randint(1, 10) # After
    while True:
        # Dibawah ini code yang salah 
        # penempatan sehingga value dari
        # "number" berubah - ubah
        #number = random.randint(1, 10) # Before
        guess =  int(input("Pick a number between 1 and 10: "))
        if guess > number:
            print("Too High")
            attempts += 1
        elif guess < number:
            print("Too Low")
            attempts += 1
        else:
            print("Just Right!")
            print(f"{attempts} attempts this round")
            return attempts

while True:
    menu = input("1: Guess the random number game\n2: Total Score\n3: Exit\n> ")
    if menu == "1":
        totalAttempts += game()
    elif menu == "2":
        print(f"You've had {totalAttempts} attempts")
    else:
        break