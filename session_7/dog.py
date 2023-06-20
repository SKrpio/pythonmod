#Creating a class 

class Dog:  #attributes
    name = "Jett"
    age = 4

    def eat(self): #behaviours
        print("nom nom")
        self.weight += 0.5
    def talk(self):
        print("bark bark") 

class Dog: 
    def __init__(self, dog_name, dog_age, dog_breed, dog_weight):  #create another class, attributes defined in dog1 below
        self.name = dog_name
        self.age = dog_age
        self.breed = dog_breed
        self.weight = dog_weight


# dog1 = Dog("Jett", 4, "pug") 
dog2 = Dog("Ninja", 13, "Dutch", 23)
print(dog2.weight)
dog2.eat()
print(dog2.age)
# print(dog1)
# print(type(dog1))
# dog1.talk()