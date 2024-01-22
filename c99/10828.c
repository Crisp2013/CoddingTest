#include<stdio.h>
#include<string.h>
int main(void)
{
	int stack[10001]={0};
	char opcode[6]={0};
	int top=0;
	int a,b,N;
	int i;
	
	scanf("%d",&N);
	
	for(i=1;i<=N;i++)
	{
		scanf("%s",opcode);
		if(strcmp(opcode,"push")==0)
		{
			scanf("%d",&a);
			top++;
			stack[top]=a;
		}
		else if(strcmp(opcode,"pop")==0)
		{
			if(top==0)
				printf("-1\n");
			else
			{
			a=stack[top];
			printf("%d",a);
			top--;
			printf("\n");
		}
		}
		else if(strcmp(opcode,"size")==0)
		{
			printf("%d",top);
			printf("\n");
		}
		else if(strcmp(opcode,"empty")==0)
		{
			switch(top)
			{
				case 0:
					printf("1");
					break;
				default:
					printf("0");
			}
			printf("\n");
		}
		else if(strcmp(opcode,"top")==0)
		{
			switch(top)
			{
				case 0:
					printf("-1");
					break;
				default:
					printf("%d",stack[top]);
			}
			printf("\n");
		}
	}
	return 0;
}