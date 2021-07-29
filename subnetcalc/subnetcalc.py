### Take subnet slash notation and convert it to a subnet mask

def subnetcalc(slash):
    #Define a string to hold the binary netmask
    binarynetmask = ""

    #Raise error if number is not within 0 and 32
    if slash > 32 or slash < 0:
        raise Exception

    #Add the slash notation as binary ones to the string
    for i in range(0, slash):
        binarynetmask += "1"
    #Then we add the zeros
    for i in range(slash, 32):
        binarynetmask += "0"
    
    #Using slicing to extract the octects from the binary
    firstbin = binarynetmask[0:8]
    secondbin = binarynetmask[8:16]
    thirdbin = binarynetmask[16:24]
    fourthbin = binarynetmask[24:32]

    #Converting every octet to decimal
    firstdec = str(int(firstbin,2))
    seconddec = str(int(secondbin,2))
    thirddec = str(int(thirdbin,2))
    fourthdec = str(int(fourthbin,2))

    return firstdec + "." + seconddec + "." + thirddec + "." + fourthdec #Return decimal netmask with dots (default)

#Subnetcalc require an int
print (subnetcalc(int(input("Enter subnet slash:"))))