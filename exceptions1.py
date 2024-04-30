class CustomExeption(Exception):

    def __init__(self):
        message = 'Divizorul nu poate fi 0!'
        Exception.__init__(self,message)

a = 4
b = [1, 0, 2]

for elem in b:
   if elem == 0:
       raise CustomExeption()
   rezultat = a/elem
   print(rezultat)