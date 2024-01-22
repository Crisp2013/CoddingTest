//#include"stdafx.h"
#include<stdio.h>
int main(void)
{
	int a, n, m, i, j, k;
	int b[31][31] = {0};
	scanf("%d", &a);
		for (i = 1; i <= a;i++)
	{
		scanf("%d %d", &n, &m);
		for (j = 0; j <= m; j++)
		{
			for (k = 0; k <= j; k++)
			{
				if (k == 0 || k == j)
					b[j][k] = 1;
				else
					b[j][k] = b[j-1][k - 1] + b[j - 1][k];
				//printf("%d", b[j][k]);
				if (j==m&&k == n)
					break;
			}
			
			//printf("\n");
		}
		printf("%d\n", b[m][n]);
	}
	return 0;
}