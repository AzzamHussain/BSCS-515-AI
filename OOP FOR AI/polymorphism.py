class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

# Function that takes any Animal object and makes it speak
def make_animal_speak(animal):
    return animal.speak()

# Creating instances of different animals
dog = Dog()
#cat = Cat()
bird = Bird()

# Calling the function with different types of animals
print(make_animal_speak(dog))   # Output: Woof!
#print(make_animal_speak(cat))   # Output: Meow!
print(make_animal_speak(bird))  # Output: Tweet!
