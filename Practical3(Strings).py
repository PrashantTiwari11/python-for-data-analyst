#😎Levle 1 Practice 
# 1. "Data Science" ki length print karo.
print (len("Data Science"))
# 2."Analytics" ka first aur last character print karo.
name = "Analytics"
print(name[0])
print(name[-1])
# 3."Python" ka third character print karo.
n1 = "Python"
print(n1[3])
# 4. ord("P") aur chr(80) ka output likho.
print(ord("P"))
print(chr(80))

# 🟡 Level 2 Practice
# 1. User se naam lo aur uska pehla aur aakhri character print karo.
name = input("Enter your name : ")
print(name[0])
print(name[-1])
# 2. User se city ka naam lo aur uski length print karo.
city = input("Enter your city name : ")
print(len(city))
# 3. User se ek character lo aur uska Unicode number print karo.
char = input("Enter your favourite character : ")
print("---Unicode of User's favourite Character---")
print(ord(char))


# 😊Practical
# 1. Apna naam store karke uske sabhi characters alag-alag print karo.
name = "Prashant"
print(len(name))
print("--Characters of my name--")
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
# 2. Apne naam ka pehla, beech ka aur last character print karo.
print(name[0])
print(name[5])
print(name[-1])
# 3. User se naam lekar uski length print karo.
name1 = input("Enter youe name : ")
print(len(name1))
# 4. User se ek character lekar uska Unicode print karo.
char = input("Enter your favourite character : ")
print("--User's charcter Unicode")
print(ord(char))
# 5. chr() use karke A-Z ke kuch characters print karo.
print(chr(80))
print(chr(82))
print(chr(85))
print(chr(87))
print(chr(92))
print(chr(99))
print(chr(83))
print(chr(93))
print(chr(94))
print(chr(95))
# 6. Multi-line address print karo using triple quotes.
print ("""
My Permanent Address
Vill- SwamiNarayan Chhapiya
Post - S.N Chhapiya
Dist - Gonda
State - Uttar Pradesh 
Pin code - 271305
Country - India
""")
# 7. id() use karke do alag strings ki identity compare karo.
print(id("Prashant"))
print(id("Tushar"))