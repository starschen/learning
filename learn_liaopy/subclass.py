class Animal(object):
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'


class Cat(Animal):
    def run(self):
        print 'Cat is running...'

class Husky(Dog):
    pass

# dog=Dog()
# dog.run()
# cat=Cat()
# cat.run()

a=list()
d=Dog()
# c=Animal()
h=Husky()

# print isinstance(a,list)
# print isinstance(d,Dog)
# print isinstance(c,Animal)
# print isinstance(d,Animal)
# print isinstance(c,Dog)
print isinstance(h,Husky)
print isinstance(h,Dog)
print isinstance(h,Animal)
print isinstance(d,Dog) and isinstance(d,Animal)

def run_twice(animal):
    animal.run()
    animal.run()

# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())

class Tortolse(Animal):
    def run(self):
        print 'Tortolse is running slowly...'

# run_twice(Tortolse())
