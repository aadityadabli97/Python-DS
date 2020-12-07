class students():

         def __init__(self,name,rollno,city):
             self.name = input(name)
             self.rollno = int(input(rollno))
             self.city = input(city)



for mystu in range(2):
    mystu=students("name","rollno","city")

    print(mystu.name)
    print(mystu.city)
    print(mystu.rollno)
