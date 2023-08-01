#Penjelsan Dictionary
""" dictName = {KeyName : KeyValue, 
    NextKeyName : NextKeyValue}
    
    Example:
    myUser = {"name": "Arres", "age": 25}
    print(dictName[keyName])
"""
""" myUser = {"name": "Arres", "age": 25}
print(myUser["name"]) """

#=================================================

""" Cara mengubah value dalam dictionary
    dictName[keyName] = keyValue
"""
#Example
""" myUser = {"name": "Arres", "age": 25}
myUser["name"] = "Joy Boy"
print(myUser["name"]) """

#=================================================

""" Sekarang kita akan mencoba membuat
    sebuah kalimat dengan f-string
"""
#Example
""" myUser = {"name": "Arres", "age": 25}
print(f"Your Name is {myUser['name']} and your age is {myUser['age']}") """

#=================================================

#Project
name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["dob"]}""")
print(f"""Tel: {contact["tel"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")