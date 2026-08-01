# 🟢 Level 1 Practice
# 1. 5 fruits ki list banao aur print karo.
fruits = ["Apple","Mango","Grapes","Pomegranet","Orange"]
print(fruits)
# 2. 5 numbers ki list banao aur second number print karo.
numbers = [10,20,30,40,50]
print(numbers[1])
# 3. Apne 3 favourite programming languages ki list banao.
program = ["Python","Java","C++"]
print(program)
# 4. Ek mixed list banao jisme String, Integer, Float aur Boolean ho.
mixed = ["Prashant",10,10.5,True]
print(mixed)
# 🟡 Level 2 Practice
# 1. User se 5 favourite movies input lekar list mein store karo.

# 2. 5 cities ki list banao aur first aur last city print karo.
cities = ["Rajkot","Surat","Noida","Delhi","Lucknow"]
print(cities[0])
print(cities[-1])
# 3. Ek list banao aur uska reverse print karo.
list = ["TUSHAR",10,52.2,True]
print(list[::-1])
# 4. Ek list mein third element ko change karo.
list = ["TUSHAR",10,52.2,True]
list[2] = 36.2
print(list)
# 🔴 Level 3 Practice
# 1. 10 students ke marks list mein store karo aur 5th mark print karo.
marks = [10,20,30,40,50,60,70,80,90,100]
print(marks[4])
# 2. Nested list banao jo 3×3 matrix represent kare.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
# 3. list1 = [10,20,30] aur list2 = list1 banao. Fir list2[1] = 999 karo aur dono lists print karke explain karo ki aisa kyu hua.
list1 = [10,20,30]
list2 = list1
print(list2)
list2[1] = 999
print(list1)
print(list2)
# 4. Ek mixed list banao aur uska len(), type() aur id() print karo.
list = ["TUSHAR",10,52.2,True]
print(type(list))
print(len(list))
print(id(list))