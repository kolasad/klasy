

class Animal:
    def __init__(self, name, age):
        """
        Konstruktor,
        Co robi ta funkcja ....
        :param name: imie zwierzaka
        :param age: wiek w latach
        """
        self.name = name
        self.age = age

    def say_name(self):
        return f'Hello {self.name}!'

    def change_name(self, new_name):
        self.name = new_name


kot = Animal('Jacek', 2)
print(type(kot))
print(kot.name)
print(kot.age)

print(kot.say_name())
kot.change_name('Kamil')
print(kot.say_name())

# print(kot.whatever)  # throws Error


class Lion(Animal):
    def roar(self):
        return 'ROARRRR!'


lion = Lion('Pan lew', 10)
print(type(lion))
print(lion.age)
print(lion.roar())

# print(kot.roar())  # Throws error
