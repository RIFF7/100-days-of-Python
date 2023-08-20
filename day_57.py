# Fungsi "reverse()"

# Code dibawah ini adalah deklarasi fungsi 
# bernama reverse yang mengambil satu argumen 
# value.
def reverse(value):
    # Code dibawah ini adalah blok kondisi pertama. 
    # Jika value kurang dari atau sama dengan 0, 
    # maka fungsi mencetak "Done!" dan kemudian 
    # mengembalikan (keluar dari rekursi).
    if value <= 0:
        print("Done!")
        return
    # Code dibawah ini adalah blok kondisi kedua. 
    # Jika value lebih besar dari 0, maka fungsi 
    # akan melakukan langkah-langkah di 
    # dalam blok ini.
    else:
        # Di dalam blok kondisi kedua, ini adalah 
        # loop for yang akan mencetak bintang (*) 
        # sebanyak value kali dalam satu baris.
        for i in range(value):
            # Baris ini mencetak bintang tanpa newline, 
            # sehingga semua bintang dicetak 
            # dalam satu baris.
            print("*", end="")
        # Setelah mencetak bintang-bintang dalam 
        # satu baris, baris ini mencetak newline 
        # (baris kosong) untuk pindah ke baris 
        # berikutnya.
        print()
        # Di dalam blok kondisi kedua, baris ini 
        # adalah rekursi. Fungsi reverse 
        # dipanggil kembali dengan nilai value - 1. 
        # Ini akan mengulangi langkah-langkah di 
        # dalam fungsi dengan value yang 
        # lebih kecil, menghasilkan pola 
        # bintang yang berkurang jumlahnya 
        # setiap barisnya.
        reverse(value - 1)
# Pemanggilan reverse(5) pada akhir kode akan 
# memulai proses rekursi dan mencetak pola bintang
reverse(5)

# Pola diatas dimulai dengan mencetak lima bintang 
# dalam satu baris dan kemudian terus berkurang 
# jumlahnya hingga mencapai kondisi akhir ketika 
# value kurang dari atau sama dengan 0, 
# di mana fungsi akan mencetak "Done!" dan 
# rekursi akan berakhir.

#================================================

# Project Factorial

# Ini adalah deklarasi fungsi factorial yang mengambil 
# satu argumen number, yang akan menjadi bilangan 
# untuk menghitung faktorialnya.
def factorial(number):
    #  Ini adalah blok kondisi pertama. 
    # Jika number adalah 1, maka faktorial dari 1 
    # adalah 1. Pada titik ini, fungsi mengembalikan 
    # nilai 1.
    if number == 1:
        return 1
    # Ini adalah blok kondisi kedua. 
    # Jika number bukan 1, maka fungsi akan melakukan 
    # langkah-langkah di dalam blok ini.
    else:
        # Di dalam blok kondisi kedua, ini adalah rekursi. 
        # Fungsi factorial dipanggil kembali dengan 
        # argumen number - 1, sehingga menghitung 
        # faktorial dari angka yang lebih kecil. 
        # Nilai ini dikalikan dengan number dan 
        # dijadikan nilai kembalian. Ini adalah dasar 
        # dari rekursi, di mana perhitungan faktorial 
        # untuk angka yang lebih besar dipindahkan ke 
        # perhitungan faktorial angka yang lebih kecil 
        # hingga mencapai basis (faktorial 1).
        return number * factorial(number - 1)
# Di sini, program meminta pengguna memasukkan angka 
# untuk menghitung faktorialnya. Input tersebut diubah 
# menjadi tipe data integer.
number = int(input("Input a number > "))
# Ini adalah pemanggilan fungsi factorial dengan 
# argumen number yang dimasukkan oleh pengguna. 
# dan disimpan pada variabel "factor"
factor = factorial(number)
# Code dibawah akan menampilkan hasim inputan dan
# perhitungan yang dilakukan pada subrutin "factorial()"
print(f"The factorial of {number} is {factor}.")