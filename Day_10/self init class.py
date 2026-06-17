class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name, "says woof")

    def eat(self, food):
        print(self.name, "eats", food.name)

class Food:

    def __init__(self, name, main_ingrident):
        self.name = name
        self.main_ingrident = main_ingrident

    def dinner_reaction(self):
        print(self.name, "is your dinner tonight")

dog1 = Dog("Max", 3)
# print(dog1.name)
# print(dog1.age)
# dog1.bark()
food1 = Food("Salmon dinner", "Salmon")

# dog1.bark()
# food1.dinner_reaction()
dog1.eat(food1)



