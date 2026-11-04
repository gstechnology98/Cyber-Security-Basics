def reciprocal(n):
    try:
        r=1/n
    except:
        print("Exception caught")
        return
    return r

print(reciprocal(10))
print(reciprocal(0))
print(reciprocal(3))