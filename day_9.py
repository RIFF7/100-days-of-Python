""" print("Generation Generator 🤭\n")

year = int(input("Which year were you born? "))

if year <= 1900:
    print("Lost Generation")
elif year <= 1927:
    print("Greatest Generation")
elif year <= 1945:
    print("Silent Geneation")
elif year <= 1964:
    print("Baby Boomers")
elif year <= 1980:
    print("Generation X")
elif year <= 1996:
    print("Millenials")
elif year < 2012:
    print("Generation Z")
else:
    print("Generation Alpha") """
    
#Cara Reple menggunakan logika AND

print("Generation Generator 🤭\n")
year = int(input("Which year were you born? "))
if year <= 1900:
    print("Lost Generation")
elif year >= 1901 and year <= 1927:
    print("Greatest Generation")
elif year >= 1928 and year <= 1945:
    print("Silent Generation")
elif year >= 1946 and year <= 1964:
    print("Baby Boomers")
elif year >= 1965 and year <= 1980:
    print("Generation X")
elif year >= 1981 and year <= 1996:
    print("Millenials")
elif year >= 1997 and year <= 2012:
    print("Generation Z")
else:
    print("Generation Alpha")