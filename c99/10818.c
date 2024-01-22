#include<stdio.h>

int main(void)
{
int N, a[1000001], MAX, MIN, i, j=0;
scanf("%d ",&N);
for(i=1;i<=N;i++)
	scanf("%d ",&a[i]);
MAX=a[1];
MIN=a[1];
for(i=2;i<=N;i++)
{
if(a[i]>=MAX)
	MAX=a[i];
else if(a[i]<=MIN)
	MIN=a[i];
}
printf("%d %d",MIN, MAX);
return 0;
}