""" myDictionary = {"name": "Ian", "health": 219, 
                "strength": 199, "equipped": "Axe"} """

#Pada code dibawah akan menampilkan KEY dari dictionary
""" for i in myDictionary:
    print(i) """

#=================================================
    
#Pada code dibawah akan menampilkan VALUE dari dictionary
""" for i in myDictionary:
    print(myDictionary[i]) """

#=================================================

""" Pada kode dibawah kita akan menggunakan
    function values() untuk menampilkan langsung
    values yang ada pada dictionary yang kita buat
"""
""" for value in myDictionary.values():
    print(value) """

#=================================================

""" Contoh lainnya adalah ketika kita akan mencoba
    menambahkan kata-kata KEYS dan VALUE 
    ditampilkan dalam output dan jika nama sama dengan 
    kekuatan (strength) maka cetak juga kata-kata
    "Whoa, SO STRONG!"
"""

""" for name, value in myDictionary.items():
    print(f"{name}: {value}")
    if name == "strength":
        print("Whoa, SO STRONG!") """

#=================================================

""" Pada contoh selanjutnya jika kita ingin menggunakan
    value pada dictionary dimana value dari strength
    kurang dari 100 maka tampilkan kata 
    "WEAK SAUCE DUDE!" kita dapat menggunakan 
    nested if dalam code, contoh dibawah ini:
"""
myDictionary = {"name": "Ian", "health": 219, 
                "strength": 99, "equipped": "Axe"}

""" for name, value in myDictionary.items():
    print(f"{name}: {value}")
    if name == "strength":
        if (value > 100):
            print("Whoa, SO STRONG!")
        else:
            print("WEAK SAUCE DUDE!") """

#=================================================

""" Jika kita hanya ingin menampilkan KEYS dan VALUE
    dari dictionary tanpa ada kata-kata tambahan
    maka kita dapat menggunakan code dibawah ini:
"""
""" for name, value in myDictionary.items():
    print(f"{name}: {value}") """

#Project
website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")