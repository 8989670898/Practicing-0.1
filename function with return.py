def food(f):
	tip=0.1*num
	f=f+tip
	fperson=f/num
	return fperson

def movie(m):
    return m/num

num=int(input("NO. of freinds: "))
ftotal=int(input("Spent on food: "))
mtotal=int(input("spent on movie:"))

x=food(ftotal)
y=movie(mtotal)
print("The per prson total is: ",x+y)
