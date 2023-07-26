# IF and ELSE

print("Marvel character Creator")
print("--")
print()
like = input("Do you like 'hanging around'?: ")
print()
voice = input("Do you have a 'gravelly' voice?: ")
print()
hero = input("Do you often feel 'Marvelous'?: ")

if like == "No":
  print("Then you're not Spider-man")
else:
  print("Then you're Spider-man")

if voice == "No":
  print("Aww, then you're not Korg")
else:
  print("Aww, then you're Korg")

if hero == "Yes":
  print("Aha! You're Captain Marvel! Hi!")
else:
  print("You're not Captain Marvel!")