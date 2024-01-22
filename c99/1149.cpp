#include<bits/stdc++.h>
using namespace std;
int main(){
    int N, i;
    int a[4][1000] = { 0 };
    int b[4],r,g,d;
    scanf("%d", &N);
    for (i = 1; i <=N; i++)
        scanf("%d %d %d", &a[1][i], &a[2][i], &a[3][i]);
    b[1] = a[1][1];
    b[2] = a[2][1];
    b[3] = a[3][1];
    for (i = 2; i <= N; i++){
        r = min(b[2], b[3]) + a[1][i];
        g = min(b[1], b[3]) + a[2][i];
        d = min(b[1], b[2]) + a[3][i];
        b[1] = r;
        b[2] = g;
        b[3] = d;
    }
    printf("%d", min(min(b[2], b[3]), b[1]));
}

