# 🟢 Level 1 Practice
# 1. Empty list banao aur usme "Python" append karo.
list = []
list.append("Python")
print(list)

# 2. [10,20] mein 30 aur 40 extend karo.
list2 = [10,20]
list2.extend([30,40])
print(list2)

# 3. "Banana" ko list ke start mein insert karo.
fruits = ["Apple","Orange","Grapes"]
fruits.insert(0,"Banana")
print(fruits)

# 4. List se "Orange" remove karo.
fruits2 = ["Banana","Apple","Orange","Grapes"]
fruits2.remove("Orange")
print(fruits2)

# 🟡 Level 2 Practice
# 1. 5 numbers ki list banao aur last element pop() karo.
nums = [10,20,30,40,50]
nums.pop(4)
print(nums)

# 2. Ek list copy karo aur prove karo ki original list change nahi hui.
list1 = [10,20,30,40,50,60]
list2 = list1.copy()
print(list2)
list2[0] = 100
print(list1)
print(list2)

# 3. Mixed list banao aur usko clear() karo.
mixed = ["Python",10,True,10.5]
mixed.clear()
print(mixed)

# 4. [90,70,80,60] ko ascending aur descending sort karo.
list3 = [90,70,80,60]
print("--Ascending Sort--")
list3.sort()
print(list3)
print("--Desending Sort--")
list3.sort(reverse=True)
print(list3)

# 🔴 Level 3 Practice
# 1. Ek shopping cart banao (list), append(), extend() aur remove() ka use karo.
list = ["Apple","Pen","Eraser","Pencil","Potato"]
print("--Append | Extend | Remove--")
list.append("Tomato")
list.extend(["Banana",100])
list.remove("Pencil")
print(list)

# 2. list1 = [1,2,3], list2 = list1, list3 = list1.copy() banao aur memory (id()) compare karo.
list1 = [1,2,3]
list2=list1
list3=list1.copy()
print(id(list1))
print(id(list2))
print(id(list3))

# 3. User se 5 subjects lo (ab append() use kar sakte ho), fir alphabetically sort karo.
subjects = []
sub1 = input("Enter Subject 1: ")
subjects.append(sub1)
sub2 = input("Enter Subject 2: ")
subjects.append(sub2)
sub3 = input("Enter Subject 3: ")
subjects.append(sub3)
sub4 = input("Enter Subject 4: ")
subjects.append(sub4)
sub5 = input("Enter Subject 5: ")
subjects.append(sub5)
subjects.sort()
print(subjects)

# 4. User se 5 numbers lo, highest aur lowest number sort karke identify karo (abhi sort() use karo, max() aur min() nahi).
nums = []
n1 = int(input("Enter Number 1: "))
nums.append(n1)
n2 = int(input("Enter Number 2: "))
nums.append(n2)
n3 = int(input("Enter Number 3: "))
nums.append(n3)
n4 = int(input("Enter Number 4: "))
nums.append(n4)
n5 = int(input("Enter Number 5: "))
nums.append(n5)
nums.sort()
print("Lowest :", nums[0])
print("Highest:", nums[-1])