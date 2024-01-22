#include<stdio.h>
int main(void){
    int t;
    int a,b;
    int i,j,k;
    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%d %d",&a,&b);
        printf("%d\n",a+b);
    }
}