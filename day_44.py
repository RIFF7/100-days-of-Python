""" Kali ini kita akan mencoba membuat tabel
    dengan fungsi input() yang nantinya value akan
    di simpan pada variabel list
"""

""" listOfshame = []

while True:
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref]
    
    listOfshame.append(row)
    
    exit = input("Exit? y/n > ")
    
    if (exit.strip().lower()[0] == "y"):
        break

print(listOfshame) """

#================================================

""" Selanjutnya bagaimana jika kita ingin menampilkan
    isi dalam tabel yang ada pada list ini
    masing-masing tanpa adanya penggabungan, contoh:
    rows 1 -> [[value 1], [value 2], [value 3]]
    rows 2 -> [[value 4], [value 5], [value 6]]
    rows 3 -> [[value n], .....]
"""
""" listOfshame = []

def prettyPrint():
    print()
    for row in listOfshame:
        print(row)
    print()

while True:
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref]
    
    listOfshame.append(row)
    
    exit = input("Exit? y/n > ")
    
    if (exit.strip().lower()[0] == "y"):
        break

prettyPrint() """

#================================================

""" Selanjutnya bagaimana jika kita ingin menampilkan
    isi dalam tabel yang ada pada list ini
    masing-masing tanpa adanya penggabungan yang
    mana menampilkan dalam bentuk list dan 
    jika kita hanya ingin menampilkannya seperti
    bentuk dalam daftar buku, contoh:
    rows 1 -> value 1 value 2 value 3
    rows 2 -> value 4  value 5 value 6
    rows 3 -> value n ..... ......]
"""

""" listOfshame = []

def prettyPrint():
    print()
    for row in listOfshame:
        for item in row:
            print(item, end="\t")
        print()
    print()

while True:
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref]
    
    listOfshame.append(row)
    
    exit = input("Exit? y/n > ")
    
    if (exit.strip().lower()[0] == "y"):
        break

prettyPrint() """

#================================================

""" Selanjutnya bagaimana jika kita ingin menampilkan
    isi dalam tabel yang ada pada list ini
    masing-masing tanpa adanya penggabungan dan
    diubah menjadi tampilan layaknya tabel, contoh:
    rows 1 -> value 1 | value 2 | value 3
    rows 2 -> value 4 | value 5 | value 6
    rows 3 -> value n | ....... |......]
"""

""" listOfshame = []

def prettyPrint():
    print()
    for row in listOfshame:
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()

while True:
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref]
    
    listOfshame.append(row)
    
    exit = input("Exit? y/n > ")
    
    if (exit.strip().lower()[0] == "y"):
        break

prettyPrint() """

#================================================

""" Selanjutnya kita akan mencoba menambahkan menu
    untuk menghapus dan menambahkan data pada
    list yang telah kita buat
    rows 1 -> value 1 | value 2 | value 3
    rows 2 -> value 4 | value 5 | value 6
    rows 3 -> value n | ....... |......]
"""

listOfshame = []

def prettyPrint():
    print()
    for row in listOfshame:
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()

while True:
    menu = input("Add or Remove Data? ")
    #Penjelasan penggunaan karakter "a"
    """ menu.strip() menghapus spasi dari input 
    pengguna untuk menghindari masalah jika ada 
    spasi tambahan di awal atau akhir input.
    
    menu.lower() mengubah seluruh karakter input 
    menjadi huruf kecil sehingga input yang 
    dimasukkan tidak tergantung pada apakah 
    diawali dengan huruf besar atau huruf kecil.
    
    [0] mengambil karakter pertama dari input 
    setelah menghapus spasi dan mengubah ke 
    huruf kecil.
    
    "a" adalah karakter yang dibandingkan 
    dengan karakter pertama yang diambil 
    dari input. """
    if (menu.strip().lower()[0] == "a"):
        name = input("What is your name? ")
        age = input("What is your age? ")
        pref = input("What is your computer platform? ")
    
        row = [name, age, pref]
        
        listOfshame.append(row)
    else:
        name = input("What is the name of the record to delete? ")
        for row in listOfshame:
            if name in row:
                listOfshame.remove(row)
                
    prettyPrint()

#Project
""" Saatnya untuk lebih banyak bingo! 
Anda dapat menggunakan kembali kode Anda 
mulai hari ke-43, tetapi kali ini tambahkan 
fitur berikut:

Berulang kali tanyakan kepada pengguna 
nomor apa yang muncul berikutnya.

Periksa kartu bingo untuk melihat 
apakah nomor yang dipilih cocok dengan 
yang ada di kartu.

Jika kartu bingo semuanya 'X', 
maka pengguna menang.
-----
Buat subrutin bernama createCard 
untuk membersihkan beberapa kode dari Hari ke-43.

Gunakan variabel dan loop untuk menyimpan 
berapa banyak x yang ada di kartu. 
Tambahkan satu setiap kali nomor diganti.

Periksa variabel setiap kali untuk melihat 
apakah sudah mencapai angka kemenangan ajaib.
"""