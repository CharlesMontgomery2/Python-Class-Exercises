userNum = int(input("Enter a number: "))
if (userNum == 1):
    print (f"{userNum} is not a prime number")
elif (userNum == 2):
    print (f"{userNum} is a prime number.")
else:
    for i in range (2, userNum):
        if (userNum % 2 == 0):
            print (f"{userNum} is not a prime number")
        else:
            print (f"{userNum} is a prime number.")
        break

############################################################



	
		



