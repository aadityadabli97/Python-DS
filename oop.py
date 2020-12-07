class Dog():                            # class is created
                                        # classname first letter should be capital ,it is called camel case
    def __init__(self,breed,name,tail):   # self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python

                 # attributes specific to self object
                    self.breed = breed
                    self.name = name
                    self.tail = tail

    def bark(self ,num):
        print(f'f string used {self.name} and my number is {num}')          #here num is not used with self because it is not related to init function

my_dog = Dog(breed='pomilion',name="tommy", tail='yes')               # my_dog is object created

print(my_dog.breed,my_dog.name,my_dog.tail)
my_dog.bark(10)


class ellipse():
    # class object attribute
    pi = 3.14

    def __init__(self,majoraxis,minoraxis):
        self.majoraxis=majoraxis
        self.minoraxis=minoraxis
        self.product_minor_major=self.majoraxis*self.minoraxis

        # method

    def area(self):
        return ellipse.pi * self.majoraxis * self.minoraxis
    def get_area_from_product(self):
        return ellipse.pi* self.product_minor_major

my_ellipse=ellipse(5,1)
print(my_ellipse.minoraxis)
print(my_ellipse.majoraxis)
print(my_ellipse.area())
print(my_ellipse.get_area_from_product())