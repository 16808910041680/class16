import random
import math
#sine and cosine calculator with imput and random number
num = int(input("Enter the angle you want us to calculate: "))
num2 = random.randint(1, 360)
print("The sine of", num, "is", math.sin(math.radians(num)))
print("The cosine of", num, "is", math.cos(math.radians(num)))
print("The sine of", num2, "is", math.sin(math.radians(num2)))
print("The cosine of", num2, "is", math.cos(math.radians(num2)))
print("The tangent of", num, "is", math.tan(math.radians(num)))
print("The tangent of", num2, "is", math.tan(math.radians(num2)))