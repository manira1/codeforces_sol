#https://codeforces.com/problemset/problem/1175/A

num = int(input())
for i in range(num):
    b, c = map(int, input().split())
    q = 0
    while(b != 0):
        aux = b//c
        q += b-(aux*c)
        b = aux
        if(aux > 0):
            q += 1

    print(q)
