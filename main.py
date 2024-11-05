import math
print ("Exercise 2 area of equilateral triangles")

lado1 = float(input("enter side A of the equilateral triangle: "))

area = ((1.7320)/4)* math.pow(lado1, 2)

if area < 1000:
    print (f"The area of the triangle is: {area} cm")
else:
    print ("INVALID DATA")
    