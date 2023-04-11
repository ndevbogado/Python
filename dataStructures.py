"""initialize a list """

myList = [1, 2, 3]
myOtherList = [4, 5]

myList.extend(myOtherList)
print(myList)

continueLoop = True
while continueLoop:
    item = input("Write some content for the next item to add to the list: (type ´no´ to exit) ")
    if item.upper() == "NO" or item.upper() == "N":
        continueLoop = False
    else:
        aux = [item]
        myList.extend(aux)

print(myList)
