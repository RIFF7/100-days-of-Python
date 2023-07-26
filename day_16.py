print(""" 
      Fill-in the blank lyrict!
      (type in the blank lyrict, see if you're as cool as me)
      """)

counter = 2
while True:
    question = input("Never going to ___ you up\n")
    if question == "give":
        counter += 1
        break
    else:
        print("Nope, try again.")
print("Well done, it only took you", counter, "attempts!")