class Duck:
    def sound(self):
        return "Quack!"

class Human:
    def sound(self):
        return "Hello!"
    
class Cat:
    def sound(self):
        return "Meow"

# Function using polymorphism
def make_sound(entity):
    print(entity.sound())

# Usage example
duck = Duck()
human = Human()
cat=Cat()

make_sound(duck)  # Output: Quack!
make_sound(human)  # Output: Hello!
make_sound(cat)#Meow
