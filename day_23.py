#Menampilkan bilangan RANDOM
""" def rolDice():
    import random
    dice = random.randint(1, 6)
    print("You Rolled", dice)

rolDice() """

#Menampilkan bilangan RANDOM dengan perulangan for
""" def rolDice():
    import random
    dice = random.randint(1, 6)
    print("You Role", dice)
    
for i in range(10):
    rolDice() """

#Tidak menggunakan operator logika    
""" print("REPLIT LOGIN SYSTEM")

def login():
    while True:
        username = input("What is your username? ")
        if username == "Arres":
            passWord = input("What is your password? ")
            if passWord == "hello":
                print("Welcome to Replit!")
                break
            else:
                print("Whoops! I don't recognize that username or password. Try again!")
        else:
            continue
            
login() """

#Menggunakan operator LOGIKA
print("REPLIT LOGIN SYSTEM")

def login():
    while True:
        username = input("What is your username? ")
        password = input("What is your password? ")
        if username == "Arres" and password == "hello":
            print("Welcome to Replit!")
            break
        else:
            print("Whoops! I don't recognize that username or password. Try again!")
            continue
login()