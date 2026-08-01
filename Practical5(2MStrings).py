# 🟢 Level 1 Practice
# 1. "Python,SQL,Excel" ko list mein convert karo.
text = "Python,SQL,Excel"
print("--Converting String to List--")
print(text.split(","))
# 2. ["Data", "Analytics"] ko "Data Analytics" banao.
text1 = ["Data", "Analytics"]
print("--Converting List to String--")
print(" ".join(text1))
# 3. Check karo "Python123" alphanumeric hai ya nahi.
text2 = "Python123"
print("--Checking for alphanumeric--")
print(text2.isalnum())
# 4. " HELLO " ko "hello" mein convert karo.
text3 = " HELLO "
print("--Removing extra spaces and converting into lowercase")
print(text3.strip().casefold())

# 🟡 Level 2 Practice
# 1. User se comma-separated subjects lo aur unhe list mein convert karo.
sub = input("Enter some subjects seperated by comma(,): ")
print("--String to List--")
print(sub.split(","))
# 2. User se 3 hobbies lo (comma separated), fir join() use karke " | " ke saath print karo.
hob = input("Enter you three hobbies : ")
hob = hob.split(",")
print("|".join(hob))
# 3. User se username lo aur check karo ki sirf alphabets hain ya nahi.
user = input("Enter your username: ")
print(user.isalpha())

# 🔴 Level 3 Practice
# 1. User se email lo aur uska username aur domain partition("@") se alag karo.
email = input("Enter your email id : ")
print(email.partition("@"))
# 2. User se full name lo aur proper format (title()) mein convert karo.
fullName = input("Enter your full name : ")
print (fullName.strip().title())
# 3. User se mobile number lo aur isdigit() se validate karo.
mobileNumber = input("Enter your phone number : ")
print (mobileNumber.isdigit())
# 4. User se password lo aur check karo:
# Sirf letters?
# Sirf numbers?
# Alphanumeric?
passw = input("Enter your password : ")
print(passw.isdigit())
print(passw.isalpha())
print(passw.isalnum())

# 📌Practical
# 1. User se CSV format data lo aur split() se list banao.
csv = input("Enter data in CSV formet : ")
print (csv.split(","))
# 2. 5 fruits ki list ko comma-separated string mein convert karo.
fruits = ['Apple','Banana','Orange','Pineapple','Pomegranet']
print(" ,".join(fruits))
# 3. Email parser banao (partition() use karke).
email = input("Enter your email id : ")
print(email.partition("@"))
# 4. Username validator (isalpha()).
user = input("Enter your username : ")
print(user.isalpha())
# 5. Mobile number validator (isdigit()).
mob = input("Enter your mobile number : ")
print(mob.isdigit())
# 6. User profile formatter (strip(), title(), casefold(), f-string).
name = input("Enter your full name : ")
age = int(input("Enter your age : "))
mob = input("Enter your mobile number : ")
email = input("Enter your email : ")
print("--User Profile--")
name = name.strip().title()
mob = mob.strip()
email = email.strip().casefold()
print(f"""
Name : {name}
Age : {age}
Mobile : {mob}
Email : {email}
""")