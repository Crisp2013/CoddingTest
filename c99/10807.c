#include<stdio.h>

int main(void)
{
int N, a[101], v, i, j=0;
scanf("%d ",&N);
for(i=1;i<=N;i++)
	scanf("%d ",&a[i]);
scanf("%d",&v);
for(i=1;i<=N;i++)
{
if(a[i]==v)
	j++;
}
printf("%d",j);
return 0;
}