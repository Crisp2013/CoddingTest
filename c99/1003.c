#include<stdio.h>

int main(void)
{
	int a, n, i, Fa[40] = { 0 }, Fb[40] = { 0 };
	scanf("%d", &a);
	while (a--)
	{
		scanf("%d", &n);
		for (i = 0; i <= n; i++)
		{
			if (i == 1)
			{
				Fa[1] = 0;
				Fb[1] = 1;
			}
			else if (i == 0)
			{
				Fa[0] = 1;
				Fb[0] = 0;
			}
			else
			{
				Fa[i] = Fa[i - 1] + Fa[i - 2];
				Fb[i] = Fb[i - 1] + Fb[i - 2];
			}
			
		}
		printf("%d %d\n", Fa[n], Fb[n]);

	}


	
}