#include<stdio.h>
int main(void){
    int t;
    int a,b;
    int i,j,k;
    // scanf("%d",&t);
    // for(i=0;i<t;i++){
    while(1){
        scanf("%d %d",&a,&b);
        if(a==0 && b==0) break;
        printf("%d\n",a+b);
    }
}