smallest = 0
largest = 0
usernum = input("Provide a number or end the process with a blank answer: ")
if usernum != "":
    number = float(usernum)
    smallest = number
    largest = number
while usernum != "":
    usernum = input("Provide a number or end the process with a blank answer")
    if usernum == "":
        break
    number = float(usernum)
    if number <= smallest:
        smallest = number
    elif number >= largest:
        largest = number
print(f"Lowest number is {smallest}")
print(f"Highest number is {largest}")




