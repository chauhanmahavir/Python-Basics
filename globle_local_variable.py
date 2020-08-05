'''x=10

def fun():
    global x
    print(x)
    x+=5
    print(x)

fun()



other method
'''
x=10

def fun():
    globx=x
    print(globx)
    globx+=5
    return globx

x=fun()
print(x)

