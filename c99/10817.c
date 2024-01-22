#include<stdio.h>

int main(void)
{
int a,b,c, n, m;
scanf("%d %d %d",&a,&b,&c);
if(a>=b)
{	
n=a;
m=b;
}
else
{	
n=b;
m=a;
}
if(c>=n)
printf("%d",n);
else if(c<m)
printf("%d",m);
else
printf("%d",c);
return 0;
}