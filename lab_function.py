def armn(x):                        #function declaration
 sum=0          
 t=x            

 while(t>0):                        #while loop starts
  d=t%10                            #we get the last number
  sum+=d**3                         #cube of above value is added to sum 
  t=t//10                           #removes remaining digits
 if sum==x:                         #value of sum is matched with x if its matched then it prints if satatement  
   return'armstrong number'
 else:
   return'not an armstrong no'      #if the values doesnt match this statement is executed
x=int(input())                      #takes input from user
print(armn(x))                      #calls functions
