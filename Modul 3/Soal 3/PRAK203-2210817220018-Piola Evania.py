a, b, i, j, x, y = input().split()
a = float(a) 
b = float(b)
i = float(i)
j = float(j)
x = float(x)
y = float(y)

print("{:.3f}\n".format((a-b)*i/j-(x+y)))

a2, b2 = input().split()
i2, j2 = input().split()
x2, y2 = input().split()
a2 = float(a2) 
b2 = float(b2)
i2 = float(i2)
j2 = float(j2)
x2 = float(x2)
y2 = float(y2)

print("{:.3f}".format((a2-b2)*i2/j2-(x2+y2)))