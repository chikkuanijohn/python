# from abc import ABC,abstractmethod
# class animal(ABC):
#     @abstractmethod
#     def make_sound(s):
#         print('sound')
# class birds(animal):
#     def fly(s):
#         print('fly')
#     def make_sound(s):
#         print('bird sound')
# class cat(animal):
#     def run(s):
#         print('run')
#     def make_sound(s):
#         print('cat sound') 
# b1=birds()
# b1.fly()
# b1.make_sound()

# print('cat')
# c1=cat()
# c1.run()

#regular expression:

# a='welcome'
# import re
# re.sub('w','W',a)
# re.sub('welcome','python',a)
# print(re.sub('welcome','python',a))
# print(re.sub('w','W',a))
# print(re.split('e',a))
# print(re.split('e',a,1))

# a='hello'
# import re
# re.sub('h','H',a)
# print(re.sub('h','H',a))
# re.split('e',a)
# print(re.split('e',a))

# a='welcome'
# import re
# re.findall('e',a)
# print(re.findall('e',a))
# len(re.findall('e',a))
# print(len(re.findall('e',a)))

# re.search('e',a)
# print(re.search('e',a))
# re.search('z',a)
# print(re.search('z',a))
# if re.search('z',a):
#     print("yes")
# else:
#     print("no")    

# if re.search('l',a):
#     print("yes")
# else:
#     print("no")  
# a='abcd'
# import re 
# re.search('d.',a)
# print(re.search('d.',a))
# re.search('b..',a)
# print(re.search('b..',a))

# re.search('d.*',a)
# print(re.search('d.*',a))
# re.search('d.+',a)
# print(re.search('d.+',a))
# re.search('d.?',a)
# print(re.search('d.?',a))


# a='welcome'
# import re
# print(re.search('e.'a))
# print(re.search('w*',a))
# print(re.search('l.+',a))
# print(re.search('c.?',a))

# import re
# a="abcd"
# re.search('[a-z]',a)
# print(re.search('[a-z]',a))
# re.search('[a-z][0-9]',a)
# print(re.search('[a-z][0-9]',a))
# a="abcd123"
# re.search('[a-z][0-9]',a)
# print(re.search('[a-z][0-9]',a))

# b="welcome"
# re.search('e$',b)
# print(re.search('e$',b))
# print(re.search('welcome',b))

# phone validation number
# import re
# a=input('enter a number')
# if len(a)==10 and a.isdigit() and re.search('[6-9].{9}',a):
#     print('valid')
# else:
#     print('invalid')


import re
a=input("enter email id:")
if re.search('[a-z].*@gmail.com',a):
    print('valid')
else:
    print('invalid')
        
 










    


















