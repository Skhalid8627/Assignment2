#Welcome Message
print("WELCOME TO ABBY'S MERCHANDIZING 'A.M' ONLINE STORE")
print("---------------------------------------------------------------------------")
print("")
print("WE SELL HIGH QUALITY CLOTHING WITH AMAZINGLY AFFORDABLE PRICES")

#Get Colour of shirt (I'll ask for 4 different colours)
print("---------------------------------------------------------------------------")
print("THIS IS OUR CATALOG OF T-SHIRTS TO CHOOSE FROM WITH A PRICE OF $9.99")
print("Please enter 'W' for WHITE")
print("Please enter 'B' for BLUE")
print("Please enter 'O' for ORANGE")
print("Please enter 'R' for RED")
print("WHAT COLOUR WOULD YOU LIKE TO PICK TODAY?")
colourofshirt = str(input())
#Using if statement to assign my variable a colour which could also be printed later
#keeping in mind that the user can enter small or Capital letter

#Validation check
for i in range(len(colourofshirt)):
    if (colourofshirt[i].isdigit() != True):
        print ("PLEASE ENTER A VALID KEY")
        colourofshirt = str(input())
    elif (colourofshirt[i].isdigit() == True):
        colourofshirt = str(input())
    else:
        colourofshirt = str(input())

if (colourofshirt == "W") or (colourofshirt == "w"):
    colourofshirt = "WHITE"
elif (colourofshirt == "B") or (colourofshirt == "b"):
    colourofshirt = "BLUE"
elif (colourofshirt == "O") or (colourofshirt == "o"):
    colourofshirt = "ORANGE"
elif (colourofshirt == "R") or (colourofshirt == "r"):
    colourofshirt = "RED"

   
#Get type of shirt (polo or t-shirt )
print("---------------------------------------------------------------------------")
print("WE OFFER TWO OPTIONS FOR OUR T-SHIRTS:")
print("1.POLO SHIRT        2.REGULAR T_SHIRT")
print("Please enter 1 for 'POLO SHIRT' OR enter 2 for 'REGULAR T-SHIRT'")
shirttype = int(input())

#As required, user will make their choice by entering either 1 or 2 (integer)
if (shirttype == 1):
    shirttype = "POLO SHIRT"
elif (shirttype == 2):
    shirttype = "REGULAR T-SHIRT"

#Get quantity of shirt
print("---------------------------------------------------------------------------")
print("HOW MANY SHIRTS WOULD YOU LIKE TO PURCHASE TODAY?")
shirtqty = int(input())


#Get Colour of pants (I'll ask for 4 different colours)
print("---------------------------------------------------------------------------")
print("THIS OUR CATALOG OF PANTS TO CHOOSE FROM WITH A PRICE OF $19.99")
print("Please enter 'G' for GREY")
print("Please enter 'B' for BLACK")
print("Please enter 'O' for ORANGE")
print("Please enter 'R' for RED")
print("WHAT COLOUR WOULD YOU LIKE TO PICK TODAY?")
colourofpants = str(input())
#Using if statement to assign my variable a colour which could also be printed later
#keeping in mind that the user can enter small or Capital letter
if (colourofpants == "G") or (colourofpants == "g"):
    colourofpants = "GREY"
elif (colourofpants == "B") or (colourofpants == "b"):
    colourofpants = "BLACK"
elif (colourofpants == "O") or (colourofpants == "o"):
    colourofpants = "ORANGE"
elif (colourofpants == "R") or (colourofpants == "r"):
    colourofpants = "RED"

#Get type of shirt (polo or t-shirt)
print("---------------------------------------------------------------------------")
print("WE OFFER TWO OPTIONS FOR OUR PANTS:")
print("1.SWEATPANTS        2.TRACKPANTS")
print("Please enter 1 for 'SWEATPANTS' OR enter 2 for 'TRACKPANTS'")
panttype = int(input())
#Validation check  
if ((panttype != 1) or (panttype != 2)):
    print ("IS THAT YOUR FINAL OPTION ?")
    panttype = int(input())
else:
    panttype = int(input())

#As required, user will make their choice by entering either 1 or 2 (integer)
if (panttype == 1):
    panttype = "SWEATPANTS"
elif (panttype == 2):
    panttype = "TRACKPANTS"

#Get quantity of pants
print("---------------------------------------------------------------------------")
print("HOW MANY PANTS WOULD YOU LIKE TO PURCHASE TODAY?")
pantqty = int(input())

#Get total quantity
totalqty = (shirtqty + pantqty)
#Declare cost of shirt and pants (CONSTANT)
SHIRTCOST = 9.99
PANTSCOST = 19.99
total = (SHIRTCOST + PANTSCOST)
totalofcost = (total * totalqty)
#Calculate the total cost before and after HST13%
tax = ((totalqty * total) * 0.13)
totalcostbeftax = ((total) * totalqty)
totalcostafttax = (totalqty * (total) + tax)

#Discounts
studentdiscounts = 0
print("ARE YOU A STUDENT ? [Y or N]")
studentdisc = str(input())
#student discount
if (studentdisc == "Y") or (studentdisc == "y"):
    studentdiscounts = (totalcostbeftax * 0.10)
totalcostafterdisc = (totalcostbeftax - (studentdiscounts))
#senior discount
seniordiscounts = 0
print("DO YOU IDENTIFY AS A SENIOR CITIZEN ? [Y or N]")
seniordisc = str(input())

if (seniordisc == "Y") or (seniordisc == "y"):
    seniordiscounts = (totalcostbeftax * 0.10)
totalcostafterdisc = (totalcostbeftax - (seniordiscounts))
#quantity discount
qtydiscounts = 0
if studentdiscounts > 0:
    seniordiscounts == 0.00
elif seniordiscounts > 0:
    studentdiscounts == 0.00
elif (shirtqty >= 3) or (seniordiscounts >= 3):
    qtydiscounts = ((totalcostafterdisc * 0.15))
elif (shirtqty <= 3) or (pantqty <= 3):
    qtydiscounts = ((totalcostafterdisc + 0))
elif (shirtqty >= 3) and (seniordisc <=3):
    qtydiscounts = ((shirtqty * SHIRTCOST)*0.15)
elif (shirtqty <= 3) and (seniordisc >=3):
    qtydiscounts = ((shirtqty * PANTSCOST)*0.15) 

totalcostafterdisctax = (totalcostafttax - qtydiscounts) - (totalcostafterdisc)



#Print receipt/Summary of the order
print("")
print("----------------------------RECIEPT-----------------------------")
print("----------------------ABBY'S MURCHANDIZING----------------------")
print("")
print("COLOUR OF SHIRT       "+ colourofshirt)
print("COLOUR OF PANT        "+ colourofpants)

print("CHOICE OF SHIRT       "+ shirttype)
print("CHOICE OF PANTS       "+ panttype)
print("QTY OF SHIRTS        ", shirtqty)
print("QTY OF PANTS         ", pantqty)
print("SENIOR DISC            $", format(seniordiscounts,".2f"))
print("QTY DISCOUNTS          $", format(qtydiscounts,".2f"))
print("STUDENT DISC           $", format(studentdiscounts,".2f"))

print("                      -----------------")
print("SUB-TOTAL              $", format(totalcostbeftax,".2f"))
print("HST 13%                $", format(tax,".2f"))
print("TOTAL COST             $", format(totalcostafttax,".2f"))
print("TOTAL DISCOUNT APPLIED $", format(totalcostafterdisc,".2f"))
print("TOTAL COST WITH DISC   $", format(totalcostafterdisc,".2f"))


