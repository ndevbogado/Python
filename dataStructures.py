"""
myList = [1, 2, 3]
myOtherList = [4, 5]

myList.extend(myOtherList)
print(myList)
"""
myList = list()
myDict = dict()
continueLoop = True
while continueLoop:
    print("""TYPE "NO" TO EXIT""")
    key = input("Write a key for a key-value pair: ")
    if key == "":
        print("Please write a none-zero key...")
        continue

    value = input("Write some content for the next item to add to the list:")

    if value.upper() == "NO" or value.upper() == "N" or key.upper() == "NO" or key.upper() == "N":
        continueLoop = False
    else:
        #aux = [int(value)]
        myDict[key]= value

#print(myList)
print(myDict.keys())
auxList = myDict.items()
commanders = []
for commander in auxList:
    commanders.extend([commander[1]])
print(commanders)
#myList.sort()
#print(myList)

