#coding: utf-8
print("Enter sum in RUB")
x = input()
y = 63.5
#x = round(x,2)
def rub2usd(x,y):
    fx = x / y
    return fx
print 'USD =', round(rub2usd(x,y),2)


