from easygui import *
import sys

while 1:
    msgbox("Welcome to flipzon")

    msg ="select the category in which you want to shop"
    title = "flipzon"                                              #give the tittle to the message box
    choices=["Mobiles", "Fashion", "kitchen", "Books"]
    choice = choicebox(msg, title, choices)
     
    msgbox("You chose: " + str(choice), "Confirm your choice")

    msg = "Do you want to continue?"                               #internal choices
    title = "Please Confirm"
    if choice=="Mobiles":                                          #every loop has adifferent section
        msgbox("Welcome to smartphone section")
        msg="Which mobile would you like to choose?"
    	title= "flipzon"                                            #give the tittle to the message box
    	choices= ["Apple iphone Xs : price=144000", "samsung galaxy s10 : price=100000 "] #internal choices
    	choice= choicebox(msg, title, choices)
        if choice=="Apple iphone Xs : price=144000":
         msg = "would you like to buy more items?"               #internal choices
         title = "Please Confirm"                                   #give the tittle to the message box
         msgbox("Thank you for buying at flipzon")
         list1.append("Apple iphone Xs : price=144000")            #adds to bill by adding in list
         sum+=144000
        elif choice=="samsung galaxy s10 : price=100000 ":
         msg = "would you like to buy more items?"               #internal choices
         title = "Please Confirm"                                  #give the tittle to the message box
         msgbox("Thank you for buying at flipzon")
         list1.append("samsung galaxy s10 : price=100000")          #adds to bill by adding in list
         sum+=100000
        msg = "would you like to buy another item?"
        title= "please confirm"                                     #give the tittle to the message box
        msgbox("thank you for buying on amazon")
    elif choice=="fashion":
        msgbox("Welcome to fashion section")
        msg="What type of clothes?"
    	title= "flipzon's Clothes section"                            #give the tittle to the message box
    	choices= ["Shirt Mens-M size-----Rs 500","top Women-M size-----Rs 500"]#internal choices
    	choice= choicebox(msg, title, choices)
        if choice=="Shirt Mens-M size-----Rs 500":  
         msg = "would you like to buy more items?"             #internal choices
         title = "Please Confirm"                                    #give the tittle to the message box
         msgbox("Thank you for buying at flipzon")
         list1.append("Shirt Mens-M size-----Rs 500")
         sum+=500
        elif choice=="top Women-M size-----Rs 500":
         msg = "would you like to buy more items?"
         title = "Please Confirm"                                 #give the tittle to the message box
         msgbox("Thank you for buying at flipzon")
         list1.append("top Women-M size-----Rs 500")                  #adds to bill by adding in list
         sum+=500 
        msg = "would you like to buy another item?"                   #internal choices
        title= "please confirm"                                   #give the tittle to the message box
        msgbox("thank you for buying on amazon")
       
       
    elif choice=="kitchen":
        msgbox("Welcome to kitchen section")
        msg="Which object?"
    	title= "flipzon's kitchen section"                           #give the tittle to the message box
    	choices= ["spatulla: price =300", "spoon set of 100 spoons: price=500"]#internal choices
    	choice= choicebox(msg, title, choices)
        if choice=="spatulla: price =300":
         msg = "would you like to buy more items?"
         title = "Please Confirm"                                       #give the tittle to the message box
         msgbox("Thank you for buying at flipzon")
         list1.append("spatulla: price =300")                           #adds to bill by adding in list
         sum+=300
        elif choice=="spoon set of 100 spoons: price=500":
         msg = "would you like to buy more items?"
         title = "Please Confirm"                                     #give the tittle to the message box
         msgbox("Thank you for buying at flipzon")
         list1.append("spoon set of 100 spoons: price=500")              #adds to bill by adding in list
         sum+=500
        msg = "would you like to buy another item?"
        title= "please confirm"                                           #give the tittle to the message box
        msgbox("thank you for buying on amazon")

        
    elif choice=="Books":
        msgbox("Welcome to book's section")
        msg="Choose your item?"
    	title="flipzon's book's section"                               #give the tittle to the message box
    	choices= ["harry potter3: price=2344", "osho the buddhist leader: price=3400"]#internal choices
    	choice= choicebox(msg, title, choices)
        if choice=="harry potter3: price=2344":
         msg = "would you like to buy more items?"                      #internal choices
         title = "Please Confirm"
         msgbox("Thank you for buying at flipzon")
         list1.append("harry potter3: price=2344")                           #adds to bill by adding in list
         sum+=2344
        elif choice=="osho the buddhist leader: price=3400":
         msg = "would you like to buy more items?"                      #internal choices
         title = "Please Confirm"
         msgbox("Thank you for buying at flipzon")
         list1.append("osho the buddhist leader: price=3400")   #adds to bill by adding in list
         sum+=3400
        msg = "would you like to buy another item?"          #internal choices
        title= "please confirm"                             #give the tittle to the message box
        msgbox("thank you for buying on flipzon")

        
    if cbox(msg,title):
       pass
    else:
        sys.exit(0)
