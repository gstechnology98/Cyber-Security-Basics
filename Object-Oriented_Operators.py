class Dogs:
    def __init__(self, name, age):
        self.name = name
        self. age = age

my_dog = Dogs("Buddy", 3)
print("Name in dog object: ", 'name' in dir(my_dog))  # Output: My dog's name is: Buddy

another_dog = Dogs("Max", 5)
print("Are same objects: ", my_dog is another_dog)  # Output: Are same objects: False

del my_dog  # Delete the my_dog object