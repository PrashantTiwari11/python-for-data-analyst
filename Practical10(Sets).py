# 🟢 Level 1 Practice
# 1. 5 fruits ka Set banao aur print karo.
fruits = {"Apple","Orange","Guava","Mango","Grapes"}
print(fruits)

# 2.Duplicate values wala Set banao aur output observe karo.
# Example: {10, 20, 20, 30, 30, 40}
numbers = {10, 20, 20, 30, 30, 40}
print(numbers)

# 3. Ek Set mein "Python" add karo using add().
subjects = {"CCT","CC","Java"}
subjects.add("Python")
print(subjects)

# 4. Set mein "SQL", "Excel", "Power BI" ek saath add karo using update().
subjects = {"CCT","CC","Java"}
subjects.update(["SQL","Excel","Power BI"])
print(subjects)

# 5. "Python" Set mein hai ya nahi check karo.
subjects = {"CCT","CC","Java","Python"}
print("Python" in subjects)

# 🟡 Level 2 Practice
# 1. Set banao aur remove() use karo.
subjects = {"CCT","CC","Java"}
subjects.remove("Java")
print(subjects)

# 2. Ek non-existing element par discard() use karo aur observe karo ki error aata hai ya nahi.
subjects = {"CCT","CC","Java"}
subjects.discard("Python")
print(subjects)

# 3. Set se pop() use karke ek element remove karo.
subjects = {"CCT","CC","Java"}
subjects.pop()
print(subjects)

# 4. Do sets banao aur unka Union nikalo.
subjects = {"CCT","CC","Java"}
subjects2 = {"CCT","CC","Java","Python"}
print(subjects | subjects2)
#print(subjects.union(subjects2)) -- using method

# 5. Do sets banao aur unka Intersection nikalo.
subjects = {"CCT","CC","Java"}
subjects2 = {"CCT","CC","Java","Python"}
print(subjects & subjects2)
#print(subjects.intersection(subjects2)) -- using method

# 🔴 Level 3 Practice
# 1.A = {10, 20, 30, 40}
#   B = {30, 40, 50, 60}
# Find: Union | Intersection | A - B & B - A | Symmetric Difference
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print("Union is : ",A | B)
print("Intersection is : ",A & B)
print("Set Difference is : ", A - B)
print("Set Reverse Difference is : ", B - A)
print("Symmetric Difference is : ", A ^ B)

# 2.Do students ke subjects ke Sets banao.
# Student A: {Python, SQL, Excel, Power BI}
# Student B: {SQL, Excel, Java, C++}
# Find:
# Dono students ke common subjects | Sirf Student A ke subjects
# Sirf Student B ke subjects | Total unique subjects
Student_A = {"Python", "SQL", "Excel", "Power BI"}
Student_B = {"SQL", "Excel", "Java", "C++"}
print("--Common subjects from both student--")
print(Student_A & Student_B)
print("--Only Student A subjects--")
print(Student_A - Student_B)
print("--Only Student b subjects--")
print(Student_B - Student_A)
print("--Total Unique Subjects--")
print(Student_A | Student_B)

# 3. Ye list hai:
# cities = [
#     "Delhi",
#     "Mumbai",
#     "Delhi",
#     "Jaipur",
#     "Mumbai",
#     "Surat",
#     "Delhi"
# ]
# Set ka use karke unique cities find karo.
cities = [
    "Delhi",
    "Mumbai",
    "Delhi",
    "Jaipur",
    "Mumbai",
    "Surat",
    "Delhi"
]
unique_cities = set(cities)
print(unique_cities)

# 4. Ek Set ko List mein convert karo, ek new element add karo, aur phir Set mein convert karo.
A = {"Python", "SQL", "Excel", "Power BI"}
my_list = list(A)
print(my_list)
my_list.append("CCT")
print(my_list)
my_set = set(my_list)
print(my_set)
