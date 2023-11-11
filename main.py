class Animal:
    name = None
    age = None
    gender = None

    def __init__(self, name='', age=0, gender=False):
        self.name = str(name)
        self.age = int(age)
        self.gender = bool(gender)


dog = Animal(name='chapi', age=2, gender=1)
print('name:',dog.name)
print('age:',dog.age)
print('gender:',dog.gender)