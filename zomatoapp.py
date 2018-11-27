from easygui import*
import sys
sum=0
while 1:
  msgbox("WELCOME,ENTER PROMO CODE AND GET 50% OFF.")
  msgbox("PROMO CODE FOR 50% OFF is='NEWS50'.")
  msg=("What  type you wanna eat ?")
  title=("Craving something,Have Something.")
  choices=["Breakfast","Indian","Chinese","Italian"]
  choice=choicebox(msg,title,choices)
  if choice=="Breakfast":
        msg1=("What  type you wanna eat,Choose a hotel ?")
        title1=("Craving something,Have Something.")
        choices1=["A1 Pizza","Smokin Joe's camp","Roll Bites"]
        choice1=buttonbox(msg1,title1,choices1)
        if choice1=="A1 Pizza":
           msg10=("Select your meal.")
           title10=("A1 Pizza") 
           choices10=["veg cheese Pizza","Special veg  paneer cheese Pizza","Special veg cheese Pizza"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="veg cheese Pizza":
              msg100=("Price is 90")
              title100=("veg cheese Pizza")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+45
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+90
           elif choice10=="Special veg  paneer cheese Pizza":
              msg100=("Price is 150")
              title100=("Special veg  paneer cheese Pizza")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150
           elif choice10=="Special veg cheese Pizza":
              msg100=("Price is 120")
              title100=("Special veg  cheese Pizza")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+60
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+120                     
        elif choice1=="Smokin Joe's camp":
           msg10=("Select your meal.")
           title10=("Smokin Joe's camp") 
           choices10=["veg cheese Pizza","Special veg  paneer cheese Pizza","Special veg cheese Pizza"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="veg cheese Pizza":
              msg100=("Price is 150")
              title100=("veg cheese Pizza")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150
           elif choice10=="Special veg  paneer cheese Pizza":
              msg100=("Price is 210")
              title100=("Special veg  paneer cheese Pizza")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+105
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+210
           elif choice10=="Special veg cheese Pizza":
              msg100=("Price is 150")
              title100=("Special veg  cheese Pizza")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150                     
        elif choice1=="Roll Bites":
           msg10=("Select your meal.")
           title10=("Roll Bites") 
           choices10=["veg cheese Pizza","Special veg  paneer cheese Pizza","Special veg cheese Pizza"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="veg cheese Pizza":
              msg100=("Price is 110")
              title100=("veg cheese Pizza")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+55
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+110
           elif choice10=="Special veg  paneer cheese Pizza":
              msg100=("Price is 100")
              title100=("Special veg  paneer cheese Pizza")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+50
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+100
           elif choice10=="Special veg cheese Pizza":
              msg100=("Price is 120")
              title100=("Special veg  cheese Pizza")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+60
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+120                     
  elif choice=="Chinese":
        msg1=("What  type you wanna eat,Choose a hotel ?")
        title1=("Craving something,Have Something.")
        choices1=["The jumbo food","Kimling Kitchen","Sky touch Chinese"]
        choice1=buttonbox(msg1,title1,choices1)
        if choice1=="The jumbo food":
           msg10=("Select your meal.")
           title10=("The jumbo food") 
           choices10=["Chicken hakka noodle","veg Schezwan rice","Chicken lollipop masala"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="Chicken hakka noodle":
              msg100=("Price is 90")
              title100=("Chicken hakka noodle")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+45
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+90
           elif choice10=="veg Schezwan rice":
              msg100=("Price is 150")
              title100=("veg Schezwan rice")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150
           elif choice10=="Chicken lollipop masala":
              msg100=("Price is 120")
              title100=("Chicken lollipop masala")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+60
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+120                     
        elif choice1=="Kimling Kitchen":
           msg10=("Select your meal.")
           title10=("Kimling Kitchen") 
           choices10=["Chicken hakka noodle","veg Schezwan rice","Chicken lollipop masala"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="Chicken hakka noodle":
              msg100=("Price is 150")
              title100=("Chicken hakka noodle")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150
           elif choice10=="veg Schezwan rice":
              msg100=("Price is 210")
              title100=("veg Schezwan rice")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+105
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+210
           elif choice10=="Chicken lollipop masala":
              msg100=("Price is 150")
              title100=("Chicken lollipop masala")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150                     
        elif choice1=="Sky touch Chinese":
           msg10=("Select your meal.")
           title10=("Sky touch Chinese") 
           choices10=["Chicken hakka noodle","veg Schezwan rice","Chicken lollipop masala"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="Chicken hakka noodle":
              msg100=("Price is 110")
              title100=("Chicken hakka noodle")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+55
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+110
           elif choice10=="veg Schezwan rice":
              msg100=("Price is 100")
              title100=("veg Schezwan rice")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+50
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+100
           elif choice10=="Chicken lollipop masala":
              msg100=("Price is 120")
              title100=("Chicken lollipop masala")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+60
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+120                     
  elif choice=="Indian":
        msg1=("What  type you wanna eat,Choose a hotel ?")
        title1=("Craving something,Have Something.")
        choices1=["Aangan veg","Bassuri","Agra restaurant"]
        choice1=buttonbox(msg1,title1,choices1)
        if choice1=="Aangan veg and nonveg":
           msg10=("Select your meal.")
           title10=("Aangan veg") 
           choices10=["Chicken tikka Masala","paneer tikka masala","Chicken pulao"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="Chicken tikka Masala":
              msg100=("Price is 90")
              title100=("Chicken tikka Masala")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+45
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+90
           elif choice10=="paneer tikka masala":
              msg100=("Price is 150")
              title100=("paneer tikka masala")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150
           elif choice10=="Chicken pulao":
              msg100=("Price is 120")
              title100=("Chicken pulao")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+60
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+120                     
        elif choice1=="Bassuri":
           msg10=("Select your meal.")
           title10=("Bassuri") 
           choices10=["Chicken tikka Masala","paneer tikka masala","Chicken pulao"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="Chicken tikka Masala":
              msg100=("Price is 150")
              title100=("Chicken hakka noodle")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150
           elif choice10=="paneer tikka masala":
              msg100=("Price is 210")
              title100=("paneer tikka masala")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+105
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+210
           elif choice10=="Chicken pulao":
              msg100=("Price is 150")
              title100=("Chicken pulao")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150                     
        elif choice1=="Agra restaurant":
           msg10=("Select your meal.")
           title10=("Agra restaurant") 
           choices10=["Chicken tikka Masala","paneer tikka masala","Chicken pulao"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="Chicken tikka Masala":
              msg100=("Price is 110")
              title100=("Chicken tikka Masala")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+55
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+110
           elif choice10=="paneer tikka masala":
              msg100=("Price is 100")
              title100=("paneer tikka masala")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+50
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+100
           elif choice10=="Chicken pulao":
              msg100=("Price is 120")
              title100=("Chicken pulao")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+60
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+120                     
  elif choice=="Italian":
        msg1=("What  type you wanna eat,Choose a hotel ?")
        title1=("Craving something,Have Something.")
        choices1=["Al saba mac mino way","cafe bistro","Jake n lerry"]
        choice1=buttonbox(msg1,title1,choices1)
        if choice1=="Al saba mac mino way":
           msg10=("Select your meal.")
           title10=("Al saba mac mino way") 
           choices10=["Alfredo pasta","Arrabiata pasta","Bistro pasta"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="Alfredo pasta":
              msg100=("Price is 90")
              title100=("Alfredo pasta")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+45
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+90
           elif choice10=="Arrabiata pasta":
              msg100=("Price is 150")
              title100=("Arrabiata pasta")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150
           elif choice10=="Bistro pasta":
              msg100=("Price is 120")
              title100=("Bistro pasta")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+60
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+120                     
        elif choice1=="cafe bistro":
           msg10=("Select your meal.")
           title10=("cafe bistro") 
           choices10=["Alfredo pasta","Arrabiata pasta","Bistro pasta"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="Alfredo pasta":
              msg100=("Price is 150")
              title100=("Alfredo pasta")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150
           elif choice10=="Arrabiata pasta":
              msg100=("Price is 210")
              title100=("Arrabiata pasta")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+105
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+210
           elif choice10=="Bistro pasta":
              msg100=("Price is 150")
              title100=("Bistro pasta")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+75
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+150                     
        elif choice1=="Jake n lerry":
           msg10=("Select your meal.")
           title10=("Jake n lerry") 
           choices10=["Alfredo pasta","Arrabiata pasta","Bistro pasta"]
           choice10=buttonbox(msg10,title10,choices10)
           if choice10=="Alfredo pasta":
              msg100=("Price is 110")
              title100=("Alfredo pasta")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+55
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+110
           elif choice10=="Arrabiata pasta":
              msg100=("Price is 100")
              title100=("Arrabiata pasta")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+50
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+100
           elif choice10=="Bistro pasta":
              msg100=("Price is 120")
              title100=("Bistro pasta")
              choices100=["ORDER","CANCEL"]
              choice100=buttonbox(msg100,title100,choices100)
              if choice100=="ORDER":
                     msg1000=("Enter promo code.")
                     title1000=("Promo code")
                     choice1000=enterbox(msg1/000,title1000)
                     if choice1000=="NEWS50":
                           msgbox("You got 50% Off")
                           sum=+60
                     else:
                        msgbox=("wrong Promo code")
                        msg10000=("Are you sure you wanna Order.You will have to pay actual price.")
                        title10000=("Be sure!")
                        choices10000=["ORDER","CANCEL"]
                        choice10000=buttonbox(msg10000,title10000,choices10000)
                        if choice10000=="ORDER":
                                     sum=+120                     
  msg = "Do you want to continue?"
  title = "Please Confirm"
  if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
  else:
	   msg="Your total is:"+str(sum)
	   title="BILL DESK"
	   textbox(msg,title)
           sys.exit(0)                                          
 


