import time
# continueLoop = True
# count = 0
# while continueLoop:
#     name = input("Enter your name (Press enter to exit): ")
#     count +=1
#     if name == '':
#         continueLoop = False
#     else:
#         print(f"(No - {count}): {name}")
# print("Good-bye!")

# startValue = int(input("Type the first value: "))
# endValue = int(input("Type the last value: "))
# while endValue <= startValue:
#     endValue = int(input(f"Please, enter a value greater than {startValue}: "))
#         
# for i in range(startValue, endValue):
#     print(i)
#
# myString = input("Write something: ") + " "
# word = ""
# for letter in myString:
#     # print(word)
    # if letter != ' ':
    #     word += letter
    # else:
    #     print(word)
    #     word = ""

duration = int(input("Duration of countdown (in secs.): "))
repeat = int(input("+Times to repeat process: ")) + 1

time.sleep(0.5)
duration *= repeat 
for seconds in range(duration, 0, -1):
    if seconds % 15 == 0:
        print(f"-- {seconds//15}th section --")
    if seconds < 10:
        print("0"+str(seconds))
    else:
        print(seconds)
    time.sleep(1)
print("Process finished!")
