MyString="Equis De"
#Dir es pa mostrar lo que se puede hacer con ese dato
#print(dir(MyString))


print(MyString.upper())
print(MyString.lower())
print(MyString.title())
print(MyString.swapcase())

print("")
print(MyString.capitalize())

print(MyString.replace("Equis","Zeta"))

print(MyString.replace("Equis","Se").capitalize())

print(MyString.count("e"))

print(MyString.startswith("Equis"))
print(MyString.endswith("De"))

#print(MyString.split("s"))
print(MyString.find("i"))
print(len(MyString))



print(f"a {MyString}")

