# inheritance

class Animal():
    def __init__(self):
        print("animal created")
    def carnivore(self):
        print("i eat meat,i have claws")
    def  herbivore(self):
        print("i eat grass,i am bunny")

my_animal=Animal()        # whenever object is created init function is called because it is a constructor
my_animal.herbivore()

class hunter(Animal):       # hunter class is inheriting Animal class

    def __init__(self):
        Animal.__init__(self)
        print('tiger created')

    def  herbivore(self):
        print("i eat grass,i am bunny,dont eat me ")      # here herbivore method is overrided

my_tiger=hunter()
my_tiger.herbivore()
my_tiger.carnivore()
print("x"*100)



# polymorphism


class dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name +' says woofs'


class cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meoww'

my_tommy=dog('tommy')
my_sally=cat("sally")
print(my_tommy.speak())
print(my_sally.speak())