
class Dog:

    def __init__(self, dog_breed="Kukis", dog_eye_color="brown and white"):
        self.breed = dog_breed
        self.eye_color = dog_eye_color


# kukis = Dog("Kukis", "brown and white")
kukis = Dog()

print(f"This dog is a {kukis.breed} and its eyes are {kukis.eye_color}")



# Example 1
# class Dog:
#
#
# def __init__(self, dogBreed, dogEyeColor):
#     self.breed = dogBreed
#     self.eyeColor = dogEyeColor
#
#
# tomita = Dog("Fox Terrier", "brown")
#
# print("This dog is a", tomita.breed, "and his eyes are", tomita.eyeColor)


# Example 2
# class Dog:
#
# def __init__(self):
#     self.nbLegs = 4
#
# tomita = Dog()
#
# print("This dog has",tomita.nbLegs,"legs")


# Example 3
# class Dog:
#
# def __init__(self, dogBreed="German Shepherd",dogEyeColor="brown"):
#
#     self.breed = dogBreed
#     self.eyeColor = dogEyeColor
#
# tomita = Dog()
#
# print("This dog is a",tomita.breed,"and his eyes are",tomita.eyeColor)