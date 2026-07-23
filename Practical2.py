# 1. Take 2 numbers from user and perfrom all arithmetic operation.
# 2. Take a number from user and check whether it is even or odd.
# 3. Take age from user and check that person is eligible for voting or not.
# 4. Take a username from user and check it is "admin" or not.
# 5. Make a list and checks 5 by using membership operator.
# 6. Make a calculator by using assignment operator. 

#Solution No. - 1
n1 = int(input("Enter your first number : "))
n2 = int(input("Enter your second number : "))
print("---ARITHMETIC OPERATIONS---")
print("1-Addition is : ",n1+n2)
print("2-Substraction is : ",n1-n2)
print("3-Multiplication is : ",n1*n2)
print("4-Division is : ",n1/n2)
print("5-Floor Division is : ",n1//n2)
print("6-Modulus is : ",n1%n2)

#Solution No. - 2
num = int(input("Enter a  number : "))
print("---Checking for even---")
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Solution No. - 3
age = int(input("Enter your age : "))
print("---Verification for voting---")
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

#Solution No. - 4
name = input("Enter your name : ")
print("---Checking For admin---")
print(name == 'admin')

#Solution No. - 5
nums = [1,2,3,4,5,6]
print("---Membership Operator---")
print(5 in nums)
print(8 in nums)
print(2 in nums)
print(1 not in nums)
print(10 not in nums)

#Solution No. - 6
num = int(input("Enter Number : "))

num += 10
print("After += :", num)

num -= 5
print("After -= :", num)

num *= 2
print("After *= :", num)

num /= 5
print("After /= :", num)