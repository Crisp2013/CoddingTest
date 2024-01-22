#include<stdio.h>
int main(void){
    int t;
    int a,b;
    int i,j,k;
    scanf("%d %d",&a,&b);
    b-=45;
    if (b<0){b+=60;a--;}
    if (a<0){a=23;}
    printf("%d %d",a,b);
}