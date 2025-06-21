class student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def greet(self):
        print(f"hi I am {self.name} and {self.age} years old.")

    def passed(self):
        return self.score > 50
    

s1 = student("abdu", 24, 66)
s2 = student("mike", 30, 40)

s1.greet()
print('passed:', s1.passed())
s2.greet()
print('passed:', s2.passed())

#inheritance

class person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'says hello')

class teacher(person):
    def teach(self):
        print(self.name, 'is teaching now')

t = teacher('mr elias')

print()
t.speak()
t.teach()

#method overiding

class kids(person):
    def speak(self):
        print(self.name, 'says I have a homework')

k = kids('baby')
print()
k.speak()