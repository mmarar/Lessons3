#coding: utf-8
print("Input x")
x = input()
x = round(x) # Как сделать чтобы введённое значение сразу округлялось?
print("Input y")
y = input()
y = round(y)
if y == 0: print("y can't be 0")
else:
    def func_div(x,y):
        fx = x / y
        return fx
    print ("Остаток от целочисленного деления x на y:", func_div(x, y))
print (x - (x / y * y)) # Остаток от деления
