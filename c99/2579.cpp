#include <bits/stdc++.h>
using namespace std;
int n,A[303],D[303][2],i; //D[i][0] = 1칸오른거
int main(){               //D[i][1] = 2칸 오른거.
    scanf("%d",&n);
    for(i=1;i<=n;i++)scanf("%d",&A[i]);
    for(i=1;i<=n;i++){
        D[i][0] = D[i-1][1]+A[i];
        D[i][1] = max(D[i-2][0]+A[i],D[i-2][1]+A[i]);
    }
    printf("%d",max(D[n][1],D[n][0]));
}
