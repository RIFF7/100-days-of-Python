# IF, ELIF and ELSE

print("MY LOGIN SYSTEM")
print("+++++++++++")

username = input("Username > ")
password = input("Password > ")

if username == "David" and password == "totallyNotBad":
  print("Why hello there David, what a lovely accent you have, you could have charned your way in here even without a password")
elif username == "Selly" and password == "hello":
  print("Have a great day")
elif username == "John" and password == "jon":
  print("Don'n forget to wear a hat in the sun!")
else:
  print("You wrong the Username and Password. Go Away!!!")