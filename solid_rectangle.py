def solid_rectangle(n,m):
    for i in range(n,n+1):
        for j in range(m,m+1):
            print("*",end="")
            print()


            rows=int(input("Enter the no. of rows:"))
            columns=int(input("Enter the no. of columns:"))
            solid_rectangle(rows,columns)

        
