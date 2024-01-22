#include<stdio.h>
#include<math.h>
#include <string.h>

double calculate(int c,int b,double a)
{
    return (10*a+b)*pow(10.0,c);
}
int scan()
{
char e[7]={0};
int a;
scanf("%s",e);
    if(!strcasecmp(e , "black"))
        a=0;
    else if(!strcasecmp(e , "brown"))
        a=1;
    else if(!strcasecmp(e , "red"))
        a=2;
        else if(!strcasecmp(e , "orange"))
        a=3;
        else if(!strcasecmp(e , "yellow"))
        a=4;
        else if(!strcasecmp(e , "green"))
        a=5;
        else if(!strcasecmp(e , "blue"))
        a=6;
        else if(!strcasecmp(e , "violet"))
        a=7;
        else if(!strcasecmp(e , "grey"))
        a=8;
        else if(!strcasecmp(e , "white"))
        a=9;
        return a;
}
int main(void)
{
    printf("%.0f",calculate(scan(),scan(),scan()));
return 0;
}
