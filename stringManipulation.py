general = "Hello There!"

print(general.upper())

#print(dir(general))

#print(help(general.zfill))

numericString = "123"
print(numericString)
numericString = numericString.zfill(10)
print(numericString)

"""
myString = input("Write a string: ")
initialRange = input("type initial range: ")
finalRange = input("type final range: ")
if initialRange == "" and finalRange == "":
    print(myString[:])
elif initialRange == "":
    finalRange=int(finalRange)
    print(myString[:finalRange])
elif finalRange == "":
    initialRange = int(initialRange)
    print(myString[initialRange:])
else:
    finalRange=int(finalRange)
    initialRange=int(initialRange)
    print(myString[initialRange:finalRange])

"""
myFloat = float(input("type a float point number: "))
message = "Type an integer to serve as a rounder for %f -- "%myFloat
print(message)
rounder = input()

roundedFloat = "%."+rounder+"f"
roundedFloat = roundedFloat % myFloat
print(roundedFloat)
