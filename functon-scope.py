x = 12 #global variable

def modify_global():
    global x  # Declare x as global to modify it
    x = 20    # Modify the global variable

modify_global()
print("global x: ", x)  # Output: global x after modification: 20 

#lambda function
square = lambda a: a ** 2
print("Square of 5: ", square(5))

#yield function 

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


for number in count_up_to(5):
    print("Generated number: ", number)  # Output: 1, 2, 3, 4, 5