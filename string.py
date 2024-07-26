a= "Arti&Choudhary!!!!!!!!!!\"Arti"
# for i in a:
#     print(i)

# print(a[:4])
b = "my name is arti choudhary"
print(len(a))
print(a.lower())
print(a.upper())
print(a.center(8))
print(a.rstrip("!"))
print(a.replace("Arti","Bebo"))
print(b.capitalize())
str1 = "His name is Dan. dan is an honest man."
print(str1.title())
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To Kill Mocking Bird"
print(str2.istitle())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Dan"))
# print(str1.index("ishh"))