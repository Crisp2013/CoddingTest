#include<stdio.h>
int main(void)
{
	int N , i;
long long a[90] = { 0 }	;
a[1] = 1;
	a[2] = 1;

	
		scanf("%d", &N);
		for (i = 3; i <= N; i++)
		{
			a[i] = a[i - 1] + a[i - 2];
		}
		printf("%lld", a[N]);
		
	
	return 0;
}