import math
import time

#formulas for cyclius
x = math.sin(time.time()/(60*60*3)*(math.pi)*2)*0.15
y = math.sin(time.time()/(60*60*12)*(math.pi)*2)*0.15
z = math.sin(time.time()/(60*60*24)*(math.pi)*2)*0.15

#figuring out if it's increasing or decreasing
a = math.cos(time.time()/(60*60*3)*(math.pi)*2)
b = math.cos(time.time()/(60*60*12)*(math.pi)*2)
c = math.cos(time.time()/(60*60*24)*(math.pi)*2)

print(x)
print("diamond")
if a < 0:
    print("decreasing")
if a > 0:
    print ("increasing")
if a == 0:
    print("extreme edge taste orz")
print(y)
print("ruby")
if b < 0:
    print("decreasing")
if b > 0:
    print ("increasing")
if b == 0:
    print("extreme edge taste orz")
print(z)
print("jade")
if c < 0:
    print("decreasing")
if c > 0:
    print ("increasing")
if c == 0:
    print("extreme edge taste orz")