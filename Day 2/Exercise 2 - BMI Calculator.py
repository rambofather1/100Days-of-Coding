# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight1 = int(weight)
height1 = float(height)

# Using the exponent operator **
bmi = weight1 / height1 ** 2
# or using multiplication and PEMDAS
bmi = weight1 / (height1 * height1)

bmi1 = int(bmi)

print(bmi1)