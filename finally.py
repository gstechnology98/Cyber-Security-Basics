def num(n):
    try:
        av = 5/n 
    except ZeroDivisionError:
        print("Exception found")
        return "not possible"
    
    else:
        print("The block is not support")
        return av
    finally:
        print("Do or die!")
    # return av
        
print(num(12))
print(num(0))
print(num(2))