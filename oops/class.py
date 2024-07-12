'''class synnefo:
    def python():
        print("python")
    def php():
        print('php')
akhil=synnefo
akhil.python()
akhil.php()'''

class synnefo:
    def __init__(self):
        print("register")
    def python(self):
        self.database="mysql"
        print("python")
    def php(s):
        print('php',s.database)

akhil=synnefo()
# manu=synnefo()
# akhil.python()
# akhil.php()        
# print(akhil.database)