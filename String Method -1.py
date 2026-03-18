'''
a = "Harry"
print(len(a))   #string are immutable 
print(a.upper())
print(a.lower())

a = "!!!Harry!!!!!!!!"
print(a.rstrip("!"))
print(a.replace("Harry" , "John"))

a = "Amit" "Mishra"
print(a.split(" "))
blogHeading  = "Introduction to JS"
print(blogHeading.capitalize())

str1 = "welcome to the cansole"
print(len(str1))
print(len(str1.center(50)))

a = "Harry", "Harry"
print(a.count("Harry"))

str1 = "This is a Laptop &&&"
print(str1.endswith("&&&"))
print(str1.endswith("is",0,7))

str1  = "He's name is sumit. He is good boy"
print(str1.find("is"))

str1 = "He's name is Mohit. He is good Athelete"
print(str1.index("Mohit"))

str1 = "WelcomeToTheCansole"
print(str1.isalnum())

str1 = "Welcome"
print(str1.isalpha())
str2 = "Welcome $$$"
print(str2.isalpha())

str1  = "hellow worldH"
print(str1.islower())

str1  = " We wish you a merry christmas\n"
print(str1.isprintable())

str1 = "   "
str2 = "       "
print(str1.isspace())
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str1 = "World Health Organization"
print(str1.isupper())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())
'''
str1 = "He's name is Amit. Amit is a good athelete"
print(str1.title())