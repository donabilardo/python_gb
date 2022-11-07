""" # Лямбда функции


from re import Match


def f(x):
    return x**2

def calc(x):
    return x+10

var = f


def math1(operation1, data1_):
    print(f, data1_)


math1(calc,100)

 """

#в качестве аргумента передаем функцию

def summ(x,y):
    return x + y

f1 = sum

def mylt(x,y):
    return x* y

f2 = mylt

def calc (oper, a, b):
    print(oper(a,b))
    #return(oper(a,b))


#calc(f2,5,5)

#print((lambda a, b: a + b)(20,40))

# 

print((lambda a, b: a if a > b else b)(333,455))