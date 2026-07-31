# 🟢 Level 1 Practice
# 1."Programming" ka reverse print karo.
text = "Programming"
print(text[::-1])
# 2."Python" ke first 4 letters print karo.
word = "Python"
print(word[:4])
# 3."banana" me "n" kitni baar hai?
text2 = "Banana"
print(text2.count("n"))
# 4."Data" ko uppercase me convert karo.
word2 = "Data"
print(word2.upper())

# 🟡 Level 2 Practice
# 1. User se naam lekar uska reverse print karo.
name = input("Enter your name : ")
print("--Reversing of user's name--")
print(name[::-1])
# 2. User se sentence lekar usme "Python" word hai ya nahi check karo.
sent = input("Enter any sentence : ")
print("--Finding 'Python' in the given sentence--")
print("Python" in sent)
# 3. User se text lekar uske extra spaces remove karo.
spaceRemove = input("Enter any text with spaces : ")
print("--Removing extra spaces--")
print(spaceRemove.strip())
#4. "Data Analytics" me sirf "Analytics" slicing se nikalo.
word3 = "Data Analytics"
print (word3.find("A"))
print (word3.find("s"))
print ("--Slicing of Word3 and removing only 'Analytics'--")
print (word3[6::])

# 🟡 Level 3 Practice
# 1. User se full name lekar uska reverse print karo.
fullName = input("Enter your full name : ")
print ("--Reversing of user's full name--")
print(fullName[::-1])
# 2. User se email lekar check karo ki "@gmail.com" se end hota hai ya nahi.
email = input("Enter your email id : ")
print("--Finding end with @gamil.com or not--")
print (email.endswith("@gmail.com"))
# 3. User se city lekar uska pehla aur aakhri character print karo.
city = input("Enter your city name : ")
print ("--Slicing first and last character of user's city--")
print (city[0])
print(city[-1])
# 4. "Data Science" me "Science" ko "Analytics" se replace karo.
repl = "Data Science"
print ("--Replacing 'Science' with 'Analytics'--")
print(repl.replace("Science","Analytics"))
# 5. "Mississippi" me "s" aur "i" kitni baar hain, count karo.
finds = "Mississippi"
print("--Finding count of 's' and 'i'--")
print(finds.count("s"))
print(finds.count("i"))
# 6. User se sentence lekar uske left aur right spaces remove karo.
spaces = input("Enter any sentences with spaces: ")
print("--Removing extra spaces from the sentences--")
print(spaces.strip())
# 7. "Python Programming" me "Programming" slicing se nikalo.
word4 = "Python Programming"
print("--Slicing 'Programming' from word4 --")
print(word4[7:])