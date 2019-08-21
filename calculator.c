#include<stdio.h>
int main()
{
int num1, num2;
    float result;
    char ch;
    printf("\n Enter the 1st number:");
    scanf("%d",&num1);
    printf("\n Enter the 2nd number:");
    scanf("%d",&num2);
    printf("Enter your operator(+,*,/,-):");
    scanf("%c",&ch);
    
    result=0;
    switch(ch)
    {
case '+':
        result=num1+num2;
        break;
case '-':
        result=num1-num2;
        break;
case '/':
        result=num1/num2;
        break;
case '*':
        result=num1*num2;
        break;
case '%':
        result=num1%num2;
        break;
   default:
        printf("Invalid Operation \n:");
    }
printf("Result: %d %c %d = %f\n",num1,ch,num2,result);
    return 0;
}