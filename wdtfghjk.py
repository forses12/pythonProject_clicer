import random
def rok(j):
    m=len(str(j))
    int(j)
    l=['','k','m','mlr','t','tlr']
    b=[]
    i=[]


    def lol():
        for s in range(0,m//3):
            if j//1000>0:
                kol()
        b.append(str(int(j)))


        for x in range(0,len(b)):
            if x==len(b)-1 or b[x]!='0':
                i.append(b[x]+l[x])

        i.reverse()
        o=' '.join(i)

        return o


    def kol():
        nonlocal j
        x=int(j%1000)
        b.append(str(x))
        j//=1000

    return lol()


