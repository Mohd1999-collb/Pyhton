
# Multilevel Inheritance example

class Animal :
    def __init__(self, voice):
        self.voice = voice

    def make_sound(self):
        print(f"The animal makes {self.voice} sound")

class Pet(Animal):
    def __init__(self, voice, name):
        super().__init__(voice)
        self.name = name

class Dog(Pet) :
    def __init__(self, voice, name) :
        super().__init__(voice, name)


    def bark(self):
        print(f"{self.name} barks: {self.voice}!")


dog = Dog("Bho Bho", "Dog")
dog.bark()