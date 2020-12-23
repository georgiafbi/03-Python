cont = "y"
while cont == "y":
    numb = int(input("How many numbers? "))

    for n in range(1,numb+1):
        print(n)

    cont = input("Would you like to continue (y)es or (n)o? ")

