#include<stdio.h>
void solid_rectangle(int n, int m)
{
int i,j;
for(i=1;i<=n;i++)
{
for(j=1;j<=n;j++)
{
print("*");
}
print("\n"):
}

}
int main()
{
int rows,columns;
printf("\nEnter the no. of rows:");
scanf("%d",&rows);
printf("\nEnter the no. of columns:");
scanf("%d",&columns);
solid_rectangle(rows,columns);
return 0;
}