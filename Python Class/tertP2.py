#x = 0
#def fac(num):
#if x == 0
#    return 1 
#else 
 #   return x*fac(x-1)#
num = int(input("Choose a number."))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)im