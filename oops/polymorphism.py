# class sample:
#     def display(self):
#         print('sample class display method')

#     def s1(self):
#         print('sample class s1 method') 

# class Demo(sample):
#     def display(self):
#         print('start')
#         print('Demo class display method')
#         super().display()

#     def d1(self):
#         print('Demo class d1 method')

# obj=Demo()
# obj.display()

# a=10
# a=12
# print(a)


# class sample:
#     def __init__(self,name,age):
#         print('sample class display method')
#         print(name,age)

#     def s1(self):
#         print('sample class s1 method') 

# class Demo(sample):
#     def __init__(self,name,age):
#         print(name,age)
#         print('start')
#         print('Demo class display method')
#         super().__init__(name,age)

#     def d1(self):
#         print('Demo class d1 method')
# obj=Demo('akhil',25)  
    
class sample:
    def display(self,name,age):
        print('sample class display method')
        print(name,age)

    def s1(self):
        print('sample class s1 method') 

class Demo(sample):
    def display(self,name,age):
        print(name,age)
        print('start')
        print('Demo class display method')
        super().display(name,age)

    def d1(self):
        print('Demo class d1 method')

obj=Demo()
obj.display('akhil',25)             


