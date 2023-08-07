mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("MokéBeast")
print()

""" Pada kode dibawah, items() digunakan untuk 
mendapatkan pasangan kunci-nilai (key-value pairs) 
dari dictionary mokedex. Fungsi items() digunakan 
dalam perulangan for untuk mengiterasi melalui 
setiap elemen dalam dictionary mokedex. """

""" Dengan menggunakan items() dan perulangan for, 
kode tersebut memungkinkan pengguna untuk mengisi 
nilai-nilai untuk setiap kunci dalam dictionary 
mokedex, sehingga mengisi dan memperbarui data pada 
dictionary dengan input yang diberikan oleh pengguna.
"""

for name, value in mokedex.items():
    mokedex[name] = input(f"{name}:\t").strip().title()

if mokedex["Type"]=="Earth":
    print("\033[32m", end="")
elif mokedex["Type"]=="Air":
    print("\033[37m", end="")
elif mokedex["Type"]=="Fire":
    print("\033[31m", end="")
elif mokedex["Type"]=="Water":
    print("\033[34m", end="")
else:
    print("\033[33m", end="")

for name, value in mokedex.items():
    print(f"{name:<15}: {value}")
