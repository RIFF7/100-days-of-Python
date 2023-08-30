# Penggunaan modul yang ada pada file lain 
# dengan memanggil nama dile tersebut pada contoh
# dibawah ini, nama dilenya adalah "test_day_63.py"
# dengan diberikan alias sebagai "test"
import test_day_63 as test

# Lalu untuk meminta modul pada file yang kita panggil
# dengan cara memanggil "nama_file.namaSubroutine(value)"
# Maka modul dari file lain akan terpanggil
test.newPrint("green")

print("Hasilnya adalah Warna Hijau")