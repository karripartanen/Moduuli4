wrong = 0
userguess = ""
passguess = ""
username = "python"
password = "rules"

while wrong < 5 or userguess != username and passguess != password:
    userguess = input("Please type in the account username: ")
    passguess = input("Type in the account password: ")
    if userguess != username or passguess != password or userguess != username and passguess != password:
        wrong = wrong+1
        print("Access denied.")
    if wrong == 5:
        print("Five tries exceeded, goodbye!")
        break
    if userguess == username and passguess == password:
        print("Access granted, welcome!")
        break
