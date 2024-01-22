#include<stdio.h>
int main(void){
    int a=0,b,c=0;
    for(int i=0;i<9;i++){
        scanf("%d",&b);
        if(b>a){
            a=b;c=i;
        }
    }
    printf("%d\n%d",a,c+1);
}