from easygui import *
import sys

while 1:
    msgbox("Welcome to flipzon")

    msg ="select the category in which you want to shop"
    title = "flipzon"
    choices=["Mobiles", "Fashion", "kitchen", "Books"]
    choice = choicebox(msg, title, choices)
     
    msgbox("You chose: " + str(choice), "Confirm your choice")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if choice=="Mobiles":
        msgbox("Welcome to smartphone section")
        msg="Which mobile would you like to choose?"
    	title= "flipzon"
    	choices= ["Apple iphone Xs : price=144000", "samsung galaxy s10 : price=100000 ", "oneplus 6t: price=50000", "nokia 6.1 plus : price=15999 "]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at flipzon")
    elif choice=="fashion":
        msgbox("Welcome to fashion section")
        msg="What type of clothes?"
    	title= "flipzon's Clothes section"
    	choices= ["Shirt Mens-M size-----Rs 500","top Women-M size-----Rs 500","Jeans Pant forMens-----Rs1000","Jeans Pant for Women-----Rs1000"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at flipzon")
    elif choice=="kitchen":
        msgbox("Welcome to kitchen section")
        msg="Which object?"
    	title= "flipzon's kitchen section"
    	choices= ["spatulla: price =300", "spoon set of 100 spoons: price=500"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at flipzon")
    elif choice=="Books":
        msgbox("Welcome to book's section")
        msg="Choose your item?"
    	title="flipzon's book's section"
    	choices= ["harry potter3: price=2344", "osho the buddhist leader: price=3400"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying on flipzon ")

    if ccbox(msg, title):    
        pass  
    else:
        sys.exit(0)
  
    msgbox("you chose"+ str(choice))
         msg="do you want to continue shopping"
         title="confirm your order"
            if ccbox(msg,tittle):
               list.append(choice)
               sum+=sum
               pass

            else 
               list.append(choice)
               sum+=sum
               textbox(msg="bill",title="bill",text=str(list)+"final="+str(sum),codebox=0)
             sys.exit(0)
