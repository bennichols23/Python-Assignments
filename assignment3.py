valid = False
cont = True
counter = 1

while (valid == False):

    userI = int(input("Enter how many users will be using the program: "))
    run = userI

    if (run < 1):
        print("Invalid input! Input must be greater then 0!")
        valid = False
    else:
        valid = True

while (counter <= run):

    subtotal = 0
    tax = 0
    taxsub = 0
    taxrate = 0
    cont = True
    itemP = 0
    itemQ = 0
    itemN = 0
    additional = " "

    while (valid == False or cont == True):
        userI = input("User "+str(counter)+", do you have"+additional+"items in your cart (Y/N): ").upper()
        valid = True

        if (userI == "Y" and valid == True):

            valid = False
            while (valid == False):
                itemN = float(input("Enter the item number (100-499): "))
                if (itemN >= 100 and itemN <= 499):
                    valid = True

                    valid2 = False
                    while (valid2 == False):
                        itemQ = float(input("Enter the quantity of the item: "))
                        if (itemQ >= 1):
                            valid2 = True

                            valid3 = False
                            while (valid3 == False):
                                itemP = float(input("Enter the price of the item: "))

                                if (itemP >= 0):
                                    valid3 = True
                                    if (itemN >= 100 and itemN <= 199):
                                        taxrate = 0
                                    elif (itemN >= 200 and itemN <= 299):
                                        taxrate = 0.05
                                    elif (itemN >= 300 and itemN <= 399):
                                        taxrate = 0.07
                                    elif (itemN >= 400 and itemN <= 499):
                                        taxrate = 0.12

                                    print("")
                                    print("Item(s) Price          "+"Item(s) Tax          "+"Item(s) total")
                                    print(str(itemP * itemQ)+"      "+str((itemP * itemQ) * taxrate)+"       "+str((itemP * itemQ) + ((itemP * itemQ) * taxrate)))

                                    subtotal = subtotal + (itemP * itemQ)
                                    tax = tax + ((itemP * itemQ) * taxrate)
                                    taxsub = taxsub + ((itemP * itemQ) + ((itemP * itemQ) * taxrate))
                                    additional = " additional "

                                    print("")
                                    print("Subtotal Before Tax          "+"Total Tax          "+"Subtotal Plus Tax")
                                    print(str(subtotal)+"      "+str(tax)+"       "+str(taxsub))
                                    print("")
                                
                                else:
                                    valid3 = False
                                    print("Invalid! Price must be a non-negative!")
                                                
                        else:
                            valid2 = False
                            print("Invalid! Must have a quantity greater then 0")
                
                else:
                    valid = False
                    print("Invalid! Item number must be between 100 and 499!")

        elif (userI == "N"):
            cont = False
            print(" ")
            if (counter == run):
                print("All users have finished. Program terminating")
            else:
                print("User "+str(counter)+" has finished, user "+str(counter+1)+", please begin.")
            counter = counter + 1
            
        else:
            print(userI+" is an invalid option! Must be Y or N!")
