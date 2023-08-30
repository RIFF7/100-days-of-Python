# OOP (Object Oriented Programming)
# Example:
# class className:
#    data and code here

# Dalam membuat class jangan lupakan identasi
# Sperti pada penempatan subroutine dari "def __init__(value)"
# Untuk code dibawah kita membuat class untuk objek hewan
class animal:
    # Di dalam kelas animal, Anda mendefinisikan tiga atribut kelas, 
    # yaitu species, name, dan sound. Ini adalah atribut yang akan 
    # dimiliki oleh setiap objek yang dibuat dari kelas ini.
    species = None
    name = None
    sound = None
    # Metode __init__: Metode ini merupakan konstruktor kelas. 
    # Ini berfungsi untuk menginisialisasi atribut-atribut objek 
    # ketika objek baru dibuat. Metode ini menerima tiga parameter: 
    # self, name, species, dan sound. Parameter self merujuk pada 
    # objek itu sendiri dan digunakan untuk mengakses dan mengubah 
    # atribut-atribut objek.
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    # Pada code dibawah menambahkan metode baru bernama talk(). 
    # Metode ini menggunakan atribut-atribut objek seperti 
    # self.name dan self.sound untuk mencetak 
    # pesan berupa ucapan hewan.
    def talk(self):
        print(f"""{self.name} says {self.sound}""")

# Inheritance = Pewarisan / Turunan

# Code dibawah mendefinisikan kelas bird dengan menggunakan 
# sintaks class bird(animal):. Tanda dalam kurung, 
# yaitu animal, menunjukkan bahwa kelas bird adalah 
# turunan dari kelas animal, sehingga kelas bird 
# akan memiliki semua atribut dan metode yang 
# telah didefinisikan di kelas animal.
class bird(animal):
    # Percobaan menambahkan variabel beru
    # dan parameter baru yatiu
    # "color"
    color = None # Variabel
    def __init__(self, color): # -> "color" Parameter
        self.name = "Bird"
        self.species = "Avian"
        self.sound = "Tweet"
        self.color = color

dog = animal("Dog", "Cihuahua", "Woof")
#print(dog.name)

# Pada code dibawah memanggil metode talk() 
# pada objek dog dengan dog.talk(). 
# Ini akan mencetak pesan "Dog says Woof".
dog.talk()

cat = animal("Kitty", "Persia", "Miaaww")
#print(cat.sound)

# Code dibawah memanggil metode talk() 
# pada objek cat dengan cat.talk(). 
# Ini akan mencetak pesan "Kitty says Miaaww".
cat.talk()

# Menampilkan value dari parameter "color"
# yaitu "Green"
polly = bird("Green")
polly.talk()
print(polly.color)

#==========================================================

# Project Inheritance

class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")

class doctor(job):
  experience = None
  speciality = None

  def __init__(self, salary, hoursWorked, experience, speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.experience = experience
    self.speciality = speciality

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.experience:<10} {self.speciality:>21}")

class teacher(job):
  subject = None
  position = None

  def __init__(self, salary, hoursWorked, subject,  position):
    self.name = "Teacher"
    self.hoursWorked = hoursWorked
    self.salary = salary
    self.subject = subject
    self.position = position
  
  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.subject:<10} {self.position:>21}")

lawyer = job("Lawyer", "$100,000", "40")
lawyer.print()

doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print()

teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.print()