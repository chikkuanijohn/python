
#appendmethod
'''f=open("new.txt","a")
f.write("python pgrm")'''

'''f=open("new.txt","r")
print(f.read())'''

'''f=open("new.txt","r")
print(f.read(5))
print('-'*20)
print(f.read(2))'''

'''f=open("new.txt","r")
print(f.readline(4))
print('-'*20)
print(f.readline(2))
print(f.readline())'''

'''f=open("new.txt","r")
print(f.readlines())
print('-'*20)'''

'''f=open("new.txt","r")
l=len(f.readlines())
f.seek(0)
for i in range(l):
    a=f.readline().strip()
print(a[::-1])'''

'''f=open("new.txt","r")
l=len(f.readlines())
f.seek(0)
word=0
for i in range(l):
    a=f.readline().strip()
    for j in a:
        if j =='':
            word+=1
    print(a[::-1])
    word+=1
print(word)'''

'''f=open("new.txt","r")
l=len(f.readlines())
f.seek(0)
word=0
letters=0
for i in range(l):
    a=f.readline().strip()
    for j in a:
        if j =='':
            word+=1
        else:
            letters+=1
    print(a[::-1])
    word+=1
    print(word)
print(letters)'''

f=open("new.txt","r")
l=len(f.readlines())
l=l
f.seek(0)
word=0
letters=0
capital=0
for i in range(l):
    a=f.readline().strip()
    for j in a:
        if j =='':
            word+=1
        else:
            letters+=1
            if j.isupper():
                capital+=1
    print(a[::-1])
    word+=1
    print(word)
    print(letters)
    print(capital)
    print(letters-capital)