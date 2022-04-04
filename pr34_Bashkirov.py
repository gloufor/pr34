1

a =int (input())
b =int (input())
c =int (input())
d =int (input())
for g in range (c,d+1):
    print('\t'+str(g),end='')
print(end='\n')
for i in range (a,b+1):
    print(str(i)+'\t',end='')
    for j in range (c,d+1):
        print(str(i*j),end='\t')
    print(end='\n')





2

a=0
while a<100:
    a =int(input())
    if a>100:
        break
    if a<10:
        continue
    print(a)

3

data =int(input())
res=0
while data !=0:
    res += data
    data = int(input())
print(res)


4

a =int(input())
b =int(input())
res =a
while res % b !=0:
    res += a
print(res)


5

a =int(input())
b =int(input())
s =0
c =0
for j in range (a, b+1):
    if j%3 == 0:
        s = s+j
        c = c+1
    j+=1
print(s/c)


6

a =  input()
s1 = a.upper().count('c'.upper())
s2 = a.upper().count('g'.upper())
S=s1+s2
print(S/len(a)*100)



7

s = [int(i) for i in input().split()]
summ = 0
l = len(s)-1
for i in range(0, 1+1):
    summ = summ + s[i]
print(summ)


10


a1 = int (input())
s= a1
s2 = 0+abs(a1**2)
while s!=0:
    a1 = int(input())
    s = s + a1
    s2 = s2+abs(a1)**2
    if s==0:
        break
print(s2)






14


def zm(n):
    dx, dy = 1, 0
    x, y = 0, 0
    arr = [[None] * n for _ in range(n)]
    for i in range(1, n**2+1):
        arr[x][y]=i
        nx, ny = x+ dx, y+ dy
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x+ dx, y+ dy
    for x in list(zip(*arr)):
        print(*x)
zm(int(input()))
        



