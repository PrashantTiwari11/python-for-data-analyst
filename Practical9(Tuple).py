# 🟢 Level 1 Practice
# 1. 5 fruits ka tuple banao.
fruits = ("Apple","Orange","Grapes","Banana","Guava")
print(fruits)

# 2. First aur last element print karo.
fruits = ("Apple","Orange","Grapes","Banana","Guava")
print(fruits[0])
print(fruits[-1])

# 3. len() use karo.
fruits = ("Apple","Orange","Grapes","Banana","Guava")
print(len(fruits))

# 4. "Apple" tuple mein hai ya nahi check karo.
fruits = ("Apple","Orange","Grapes","Banana","Guava")
print("Apple" in fruits)

# 🟡 Level 2 Practice
# 1. Marks tuple ka sum(), min(), max() print karo.
marks = (10,20,30,40,50)
print(sum(marks))
print(min(marks))
print(max(marks))

# 2. Second aur third element slicing se print karo.
marks = (10,20,30,40,50)
print(marks[1:3])

# 3. Tuple ka count() use karo.
marks = (10,20,30,40,50)
print(marks.count(20))

# 4. Tuple ka index() use karo.
marks = (10,20,30,40,50)
print(marks.index(20))

# 🔴 Level 3 Practice
# 1. Student tuple banao (name, age, course) aur unpack karo.
student = ("Prashant",21,"CE")
print(student)
#Unpacking
name , age , course = student
print(name) 
print(age) 
print(course) 

# 2. Nested tuple banao aur center value print karo.
metrics = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
print(metrics[1][1])

# 3. List ko tuple mein convert karo aur type check karo.
nums = [10,20,30]
t = tuple(nums)
print(t)
print(type(t))

# 4. Tuple ko list mein convert karo, ek value add karo aur phir wapas tuple bana do.
t = (10,20,30)
nums = list(t)
print(t)
print(type(t))
print("--------")
nums.append(40)
print(nums)
print("List to Tuple")
t = tuple(nums)
print(t)
print(type(t))