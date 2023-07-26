"""
      Penggunaan kalimat panjang dengan 3 tanda kutip, serta pewarnaan pada text
      yang dapat dilihat pada folder Color_for_text.txt untuk code warnanya
"""

print("""
Welcome to your adventure simulator. 
I am going to ask you bunch of questions and then create an epic story with you as the star!
""")
name = input("What is your name? ")
enemy = input("What is your worst enemy's name? ")
power = input("What is your superpower? ")
live = input("Where do you live? ")
food = input("What is your favorite food? ")
print()
print("Hello", "\033[32m", name, "\033[0m", "Your ability to", 
      "\033[33m", power, "\033[0m", "will make sure you naver have to look at", 
      "\033[31m", enemy, "\033[0m", "again. Go eat", "\033[34m", food, 
      "\033[0m", "as you walk down the streets of", "\033[36m", live, 
      "\033[0m", "and use", "\033[35", power, "\033[0m", "for good and not evil!")