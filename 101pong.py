#!/usr/bin/python3
import math
import sys

def hypotenuse(xv,yv,zv) :
    return (math.sqrt((xv * xv) + (yv * yv) + (zv * zv)))

if len(sys.argv) != 8 :
    sys.exit(84)

i = 1

while i < len(sys.argv) :
    j = 0
    while j < len(sys.argv[i]) :
        if ord(sys.argv[i][j]) < ord('-') or ord(sys.argv[i][j]) > ord('9') :
            sys.exit(84)
        j = j + 1
    i = i + 1
    
i = 7
j = 0

while j < len(sys.argv[i]) :
    if ord(sys.argv[i][j]) < ord('0') or ord(sys.argv[i][j]) > ord('9') :
        sys.exit(84)
    j = j + 1
                                             
x0 = float(sys.argv[1])
y0 = float(sys.argv[2])
z0 = float(sys.argv[3])
x1 = float(sys.argv[4])
y1 = float(sys.argv[5])
z1 = float(sys.argv[6])
n = int(sys.argv[7])

if n < 0 :
    sys.exit(84)
    
xv = x1 - x0
yv = y1 - y0
zv = z1 - z0

xn = x1 + xv * n
yn = y1 + yv * n
zn = z1 + zv * n

adjacent = z1 - z0
error = hypotenuse(xv,yv,zv)

if error == 0 or adjacent == 0 :
    print("The velocity vector of the ball is:")
    print("(%.2f, %.2f, %.2f)" % (xv, yv , zv))
    print("At time t + %d, ball coordinates will be:" % (n))
    print(xn, yn, zn)
    print ("The ball won't reach the paddle.")
    sys.exit(0)
    
result = math.degrees(math.acos(adjacent / hypotenuse(xv, yv, zv))) - 90

print("The velocity vector of the ball is:")
print("(%.2f, %.2f, %.2f)" % (xv, yv , zv))
print("At time t + %d, ball coordinates will be:" % (n))
print(xn, yn, zn)

if result < 0 or result > 90 :
    print ("The ball won't reach the paddle.")
elif zv > 0 and z1 <= 0 :
    print("The incidence angle is:")
    print("%.2f degrees" % result)
elif zv < 0 and z1 >= 0 :
    print("The incidence angle is:")
    print("%.2f degrees" % result)
else :
    print ("The ball won't reach the paddle.")
