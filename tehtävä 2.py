Inch = 0
inchToCM = 0
while Inch >= 0:
    Inch = float(input("Provide the length in inches: "))
    if Inch >= 0: #terminates the program if the user provides a negative number
        inchToCM = (Inch*2.54) #converts inches to centimeters
        print(f"{Inch} inches is {inchToCM} centimeters.")
