class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age    

    def __str__(self):
        return f'my name is {self.name} and i am {self.age} years old'
    def is_adult (self) :
        if self.age >= 18 :
            return 'You have too much responsibilities '
        else :
            return 'lucky'

first_person = Person('hoor', 14)
print(first_person)