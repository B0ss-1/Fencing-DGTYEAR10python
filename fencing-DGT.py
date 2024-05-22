# Fencing cauclater
# Author: Barnaby walker 
# Date 22/05/2024
# Verson: 1.01

print("Instuctions:")
print()
print("Enter the price of the fencing per meter.")
print("After that enter the width and length.")
print("Then this program will cauclate the peremeter.")
print("and cost of fencing of the land you wanted to")
print("find the price of fencing off.")
print()
def number_check(Question):
    Deaththreat="Put in a number bigger than 0. Or else.\n"
    while True:
        try:
            number=float(input(Question))
            if number>0:
                return number
            else:
                print(Deaththreat)
        except ValueError:
            print(Deaththreat)
keepgoing="Y"
while keepgoing=="Y":
    price=number_check("Price per meter of fence: $")
    width=number_check("Width: ")
    length=number_check("Length: ")
    perimeter=(width+length)*2
    cost=(perimeter)*price
    print()
    print(f"Fencing pricing = ${cost} ")
    keepgoing=input("Continue? Y/N ")
    print()
    if keepgoing!=("N"):
        keepgoing="Y"
print("Thank you for using this program, please consider donating to Fencing Caulater NZ.")
