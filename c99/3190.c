#include<stdio.h>

typedef struct _Pos{
    int x;
    int y;
}Pos;



int main(void)
{
    //int map[100][100]={0};
    int MapSize;

    int AppleCount;
    Pos ApplePosition[100];

    int DirectionChangeCount;
    struct _DirectionChange{
        int time;
        char direction[2];
    };
    struct _DirectionChange DirectionChange[100];
    int DirectionChangeCurrent=0;

    int SnakeLength=1;
    Pos SnakePosition[101];

    int CurrentTime=0;

    int CurrentDirection=1;
    //0=북
    //1=동
    //2=남
    //3=서
    int i,j,k;

    scanf("%d",&MapSize);
    scanf("%d",&AppleCount);
    for(i=0;i<AppleCount;i++) scanf("%d %d",&ApplePosition[i].x, &ApplePosition[i].y);
    scanf("%d",&DirectionChangeCount);
    for(i=0;i<DirectionChangeCount;i++) scanf("%d %s",&DirectionChange[i].time, DirectionChange[i].direction);

    SnakePosition[0].x=SnakePosition[0].y=1;

    for(CurrentTime=1;;CurrentTime++)
    {

        Pos newPos;
        if(CurrentDirection==0)
        {
            newPos.x=SnakePosition[0].x-1;
            newPos.y=SnakePosition[0].y;
        }
        else if(CurrentDirection==2)
        {
            newPos.x=SnakePosition[0].x+1;
            newPos.y=SnakePosition[0].y;
        }
        else if(CurrentDirection==1)
        {
            newPos.x=SnakePosition[0].x;
            newPos.y=SnakePosition[0].y+1;
        }
        else if(CurrentDirection==3)
        {
            newPos.x=SnakePosition[0].x;
            newPos.y=SnakePosition[0].y-1;
        }
    //  printf("[%d %d].%d.%d \n",newPos.x,newPos.y, CurrentDirection, SnakeLength);//debug

        if(newPos.x == 0 || newPos.x == MapSize+1 || newPos.y == 0 || newPos.y == MapSize+1)
        {
            printf("%d", CurrentTime);
            return 0;
        }

        for(i=0;i<AppleCount;i++)
        {
            if(newPos.x == ApplePosition[i].x && newPos.y==ApplePosition[i].y){
                SnakeLength++;
                ApplePosition[i].x=ApplePosition[i].y=-1;
                break;
            }
//          printf("<%d %d>",ApplePosition[i].x,ApplePosition[i].y);
        }


        if(SnakeLength>=1)
        {
            for(i=SnakeLength;i>=1;i--)
            {
                SnakePosition[i].x=SnakePosition[i-1].x;
                SnakePosition[i].y=SnakePosition[i-1].y;
                if(SnakePosition[i].x == newPos.x && SnakePosition[i].y==newPos.y)
                {
                    printf("%d", CurrentTime);
                    return 0;
                }
            }
        }
        SnakePosition[0].x=newPos.x;
        SnakePosition[0].y=newPos.y;
        if(CurrentTime==DirectionChange[DirectionChangeCurrent].time && DirectionChangeCurrent<DirectionChangeCount)
        {
            if(DirectionChange[DirectionChangeCurrent].direction[0]=='D')
                CurrentDirection=(CurrentDirection+1)%4;
            else
                CurrentDirection=(CurrentDirection+3)%4;
            DirectionChangeCurrent++;
        }
    }
    return 0;
}