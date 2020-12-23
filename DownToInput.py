name = input("What is you name? ")
neighborName = input("What is your neighbor's name? ")

codeExp = int(input("How many months have you been coding? "))
codeExpNeighbor=int(input("How many months has your neighbor been coding? "))
print(f"My name is {name} and I have been coding for {codeExp} months")
print(f"My neighbor's name is {neighborName} and they have been coding for {codeExpNeighbor} months")
print(f"Together we have been coding for {codeExp+codeExpNeighbor} months")