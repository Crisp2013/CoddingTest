n = int(input())

def isPrime(num):
    global primes
    if num<=1:
        return False
    if num==2:
        return True
    for i in primes:
        if i == 0:
            continue
        if int(num**0.5)<i:
            break
        if num%i==0:
            return False
    return True

maps = [0]*(n+1)
primes = [2]
for i in range(3,n+1,2):
    if isPrime(i):
        primes.append(i)
# print(primes)


s, e = 0, 0
answer = 0
sum=2
while True:
    # print(primes[e],primes[s],sum)
    if sum<n:
        if e == len(primes)-1:
            break
        e+=1
        sum+=primes[e]
    elif sum>=n:
        if sum==n:
            answer+=1
        if s == len(primes)-1:
            break
        sum-=primes[s]
        s+=1
print(answer)

