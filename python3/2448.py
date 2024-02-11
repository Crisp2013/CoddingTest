n = int(input())

a=["  *   "," * *  ","***** "]

#1
#11
#101
#1111
#10001
#110011

frac = [1]


for i in range(1, n//3+1):

    for j in range(3):
        for k in range((n-3*i)):
            print(" ", end="")
        for k in range(i):
            if frac[k]==1:
                print(a[j], end="")
            else:
                print("      ", end="")
        for k in range((n-3*i)):
            print(" ", end="")
        print()
    
    frac_new = [0] * (i+1)
    for i in range(len(frac)):
        frac_new[i]=(frac_new[i]+frac[i])%2
        frac_new[i+1]=(frac_new[i+1]+frac[i])%2
    frac = frac_new