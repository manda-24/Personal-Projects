from numpy import binary_repr


"""list1 = []
while True:
    a = input("Enter a number: ")
    if a == "p": 
        print(list1)


    elif a == "s":
        print("The minimum value is: ", min(list1))
        print("The maximum value is: ", max(list1))
        print("The average value is: ", sum(list1)/len(list1))


    elif a == "x" or a == "q": 
        print("The minimum value is: ", min(list1))
        print("The maximum value is: ", max(list1))
        print("The average value is: ", sum(list1)/len(list1))
        quit()
    
    #Use quit() or exit()

    elif a.isnumeric(): 
        list1.append(float(a))
        print(list1)

    else: 
        print("Error. Enter a valid number")"""


#A function that takes a number as an input and returns the binary representation. 

b = int(input("Enter a number: "))

def to_binary(b): 
    binary = bin(b)
    print(binary)

hello = to_binary(b)