s=("hello")
c=0
while(c<5):
	t=input("enter password:")
        if (t==5):
        	print("you are logged in")
        	break
        else:
        	print("re-enter the password")
		c=c+1

        if(c==5):
		print("your all attempts are failled")
