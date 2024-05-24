# Fencing cauclater
# Author: Barnaby walker 
# Date: 24/05/2024
# Version: 1.2

print("Instuctions:")
print()
print("Enter the price of the fencing per meter.")
print("After that enter the width and length.")
print("Then this program will cauclate the perimeter.")
print("and cost of fencing of the land you wanted to")
print("find the price of fencing off.")
print()
def number_check(question):
    deaththreat="Put in a number bigger than 0. Or else.\n"
    while True:
        try:
            number=float(input(question))
            if number>0:
                return number
            else:
                print(deaththreat)
        except ValueError:
            print(deaththreat)
keepgoing=""
while keepgoing=="":
    price=number_check("Price per meter of fence: $")
    width=number_check("Width: ")
    length=number_check("Length: ")
    perimeter=(width+length)*2
    cost=(perimeter)*price
    print()
    print(f"Fencing pricing = ${cost}")
    keepgoing=input("Continue? Press enter to continue. ")
    print()
print("Thank you for using this program, please")
print("consider donating to Fencing Caulater NZ.")
