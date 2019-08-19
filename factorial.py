#calculate factorial

num=int(input("Enter a number: "))
fact=1
for x in range(1, num+1) :
    fact=fact*x
print ("The factorial of {} is {}".format(num,fact))
