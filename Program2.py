#coding: utf-8
print('Input x')
x = float(input())
print('Input y')
y = input()
z = x - y
if z == 0:
    print ("Division by 0")
    pass
else:
    print '(x+y)/(x-y)=', ((x+y)/z)
