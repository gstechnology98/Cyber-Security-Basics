for i in range(1,11):
    if(i%2!=0):
        print("Break values: ", i)
        break
    print(i)


while i in range(1,11):
    if i%3==1:
        print("Continues value: ", i)
        i+=1
        continue
    print(i)
    i+=1