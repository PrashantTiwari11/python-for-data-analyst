# 🟢 Level 1 Practice
# 1. 5 numbers ki list banao aur len() print karo.
nums = [10,20,30,50,40]
print(len(nums))
# 2. Marks list ka sum() print karo.
marks = [50,70,80,90,100]
print(sum(marks))
# 3. min() aur max() use karo.
marks = [50,70,80,90,100]
print(min(marks))
print(max(marks))
# 4. Do lists ko + se jodo.
nums = [10,20,30,50,40]
marks = [50,70,80,90,100]
print(nums + marks)
# 🟡 Level 2 Practice
# 1. Ek list ko sorted() aur sort() dono se sort karke difference dikhao.
marks = [90, 50, 80, 70]
marks2 = sorted(marks)
print(marks)   # Original list
print(marks2)  # Sorted copy

# 2. "Python" list mein hai ya nahi check karo.
sub = ["CCT","Python","Cloud Computing"]
print("Python" in sub)
# 3. [10] * 5 ka output print karo.
print([10]*5)
# 4. Nested list banao aur second row print karo.
metrics = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(metrics[1])
# 🔴 Level 3 Practice
# 1. 5 students ke marks ki list banao aur average calculate karo (sum() aur len() se).
stu_marks = [50,60,80,95,88]
average = sum(stu_marks)/len(stu_marks)
print(average)

# 2. 3×3 matrix banao aur center element print karo.
metrics = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(metrics[1][1])

# 3. list1 = [1,2,3] aur list2 = sorted(list1) banao. Fir list2 change karke prove karo ki list1 change nahi hui.
list1 = [1,2,3]
list2 = sorted(list1)
print(list1)
print(list2)
list2.append(10)
print(list2)
print(list1)
# 4. Ek shopping list aur ek stationery list banao, dono ko merge karo aur alphabetical order mein print karo.
shop_list = ["Clothes","Socks","T-Shirt"]
stat_list = ["Pencil","Sharpner","Eraser"]
shopping = shop_list + stat_list
shopping = shopping.sort()
print(shopping)