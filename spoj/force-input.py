
import os

while True:
    number = input()
   
    number = int(number)
    if isinstance(number,int) and number in range(0,100) and number != 42:
            # print(number)
            pass
    else:
        print("please input integer number >=0 and <100 and not =42")
        os._exit(1)
