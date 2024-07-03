'''a=20
def fun1():
    a=15
    a=a+10
    print('welcome',a)
fun1()
print('outsidefun',a)'''

'''a=20
def fun1():
    global b
    b=10
    print('welcome',b)
fun1()
print('outsidefun',b)'''

a=20
'''def fun1():
    global b
    b=10
    print('welcome',b)
    c=25
    return c,74
c1,d1=fun1()
print('outsidefun',c1,d1)'''

'''def add(a,b):
    return a+b
print(add(10,20))
print(add(10,30))
print(add('asd','a2123'))'''

'''def add(name,age=24):
    return name,age
print(add('anu',25))
print(add('sanu'))'''

'''def add(name,age):
    print("name:",name)
    print("age:",age)
add('anu',25)
add(age=24,name='sanu')'''

'''def add(*a):
    return a
print(add('anu',25))
print(add())'''

def add(**a):
    return a
print(add(name='anu',age=25))
print(add())
