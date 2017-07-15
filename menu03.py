############
#
#       Menu02
#   Gavin Tynan
#
############
#
#   Variables
#
yes = "yes"
no = "no"
optionOne = "Vegetarian Sub"
optionTwo = "Spinach Salad"
optionThree = "Fruit Salad"
optionFour = "Tuna Salad"
dSpec = "Artichoke & Walnut Salad"
msgMultOrders = "Would you like to order more (yes or no)? "
msgSelect = "Thank you for selecting "
msgTime = "Your order will be ready in approximately "
msgPrice = "The total of your order so far is "
msgSpec = "Please vist NutriCafe again and consider a Daily Special."
optionOneTime = "3 minutes."
optionTwoTime = "2 minutes."
optionThreeTime = "3 minutes."
optionFourTime = "3 minutes."
dSpecTime = "5 minutes."
optionOnePrice = 6.50
optionTwoPrice = 7.00
optionThreePrice = 6.00
optionFourPrice = 5.75
dSpecPrice = 7.50
totalCost = 0
itemsOrdered = 0
menuCont = ""
#   choice = userInput
############
print "*********************************************"
print
print "*"
print
print "*    Welcome to the NutriCafe"
print
print "*"
print
print "*********************************************"
print

while menuCont != no:
    itemsOrdered = itemsOrdered + 1
    print "Today's Daily Special:"
    print
    print "***********************"
    print
    print "*    DAILY SPECIAL    *"
    print
    print "***********************"
    print dSpec
    print
    print
    print
    print
    print "***********************"
    print
    print "*        MENU         *"  
    print
    print "***********************"
    print
    print ("1) " + optionOne + " - " + str(format(optionOnePrice,".2f")))
    print
    print ("2) " + optionTwo + " - " + str(format(optionTwoPrice,".2f")))
    print
    print ("3) " + optionThree + " - " + str(format(optionThreePrice,".2f")))
    print
    print ("4) " + optionFour + " - " + str(format(optionFourPrice,".2f")))
    print
    print ("5) " + dSpec + " - " + str(format(dSpecPrice,".2f")))
    print
    choice = input("Please Enter a Choice --> ")
    print
    if choice == 1:
        print (msgSelect + optionOne)
        totalCost = optionOnePrice + totalCost 
        print (msgPrice + "$" +(str(format(totalCost,".2f"))))
    elif choice == 2:
        print (msgSelect + optionTwo)
        totalCost = optionTwoPrice + totalCost 
        print (msgPrice + "$" + (str(format(totalCost,".2f"))))
    elif choice == 3:
        print (msgSelect + optionThree)
        totalCost = optionThreePrice + totalCost 
        print (msgPrice + "$" + (str(format(totalCost,".2f"))))
    elif choice == 4:
        print (msgSelect + optionFour)
        totalCost = optionFourPrice + totalCost 
        print (msgPrice + "$" + (str(format(totalCost,".2f"))))
    elif choice == 5:
        print (msgSelect + dSpec)
        totalCost = dSpecPrice + totalCost 
        print (msgPrice + "$" + (str(format(totalCost,".2f"))))
    menuCont = raw_input("Would you like to order more ('yes' or 'no')")
if itemsOrdered == 1:
    print ("You have ordered 1 item and the total was $ " + (str(format(totalCost,".2f"))))
else:
    print ("You have ordered " + str(itemsOrdered) + " items and the total was $ " + (str(format(totalCost,".2f"))))
