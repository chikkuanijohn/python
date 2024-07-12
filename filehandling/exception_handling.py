
'''try:
    a=int(input("enter no"))
    print(a)
except:
    print("input a no")'''

'''while True:
    try:
        a=int(input("enter no"))
        print(a)
        break
    except:
        print("input a no")'''

try:
    print('10'+'abc')
except NameError:
    print('its name error')
except TypeError:
    print('its type error')
else:
    print('else')
finally:
    print("finally")


    




