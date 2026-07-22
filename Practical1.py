# 1. Take name , age , city from user and print it .
# 2. Take two number from user and add them .
# 3. Take length and width from user and find area of rectangle.
# 4. Take radius of a circle from user and find area of circle.
# 5. Take Celsius as a input and convert it into Fahrenheit.
# 6. Take Fahrenheit as a input and convert it into Celsius.
# 7. Take marks of 5 subjects from user and find toal & average of all subject's marks .

#Solution-1 
name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter your city : ")
print()
print("---Basic Details---")
print("Name : ",name)
print("Age : ",age)
print("City : ",city)

#Solution-2
num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
print("---Addition Of Two Numbers---")
print(num1 + num2)

#Solution-3 
length = int(input("Enter your length : "))
width = int(input("Enter your width : "))
print()
print("---Area Of Rectangle---")
print("Area of Rectangle = ",length * width)

#Solution-4 
radius = float(input("Enter Radius : "))
print("---Area of Circle---")
print(3.14*radius*radius)

#Solution-5 
celsius = int(input("Enter celsius degree : "))
print ("---Conversion from Celsius to Fahrehiet---")
print ((celsius*1.8)+32)

#Solution-6 
fahrenhiet = int(input("Enter Fahrenheit degree : "))
print ("---Conversion from Fahrenheit to Celsius---")
print ((fahrenhiet-32)*1.8)

#Solution-7 
m1 = int(input("Enter mark 1 : "))
m2 = int(input("Enter mark 2 : "))
m3 = int(input("Enter mark 3 : "))
m4 = int(input("Enter mark 4 : "))
m5 = int(input("Enter mark 5 : "))
print()
print("---Average of all marks---")
print((m1+m2+m3+m4+m5)/5)
print("---Total of all marks---")
print(m1+m2+m3+m4+m5)