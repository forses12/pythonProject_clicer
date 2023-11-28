import random
def rok(j):
    m=len(str(j))
    l=['k','m','mlr','t','tlr']
    b=[]


    def lol():
        for s in range(0,m//3):
            if j//1000>0:
                kol()
        b.append(str(j))

        if m%3==0:
            for x in range(0, m // 3-1):
                b[x] = l[x] + ' ' + b[x]
        else:
            for x in range(0, m // 3):
                b[x] = l[x] + ' ' + b[x]

        b.reverse()
        o=''.join(b)
        return o


    def kol():
        nonlocal j
        x=str(j%1000)
        b.append(x)
        j//=1000

    return lol()
