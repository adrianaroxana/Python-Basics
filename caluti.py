class Horse:
    def __init__(self, name, breed, age, color, sex):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.sex = sex


horse1 = Horse("Spirit", "Mustang", "2", "beige", "male")
horse2 = Horse("Flower", "Arabian", "2", "light brown with white spots", "female")

print(horse1.breed)
print(horse2.name)
