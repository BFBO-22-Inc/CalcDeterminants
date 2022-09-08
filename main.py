def msp(i):
    return list(map(int, i.split(" ")))


def msl(i):
    return list(map(str, i.split('!')))

def cds(i,a,b):
    return msp(msl(i)[a])[b]

def BdInStr(l):     #Преобразование двучмерного списка в строчку
    bs=""
    for q in l:
        for w in q:
            bs+=str(w)+' '
        bs=bs[:-1]+'!'
    return bs[:-1]

def oper(s,n):
    if n==2:
        return cds(s,0,0)*cds(s,1,1)-cds(s,0,1)*cds(s,1,0)
    sun=0
    for q in range(n):
        local = []
        for w in msl(s)[1:]:
            localest=[]
            for e in range(n):
                if e!=q:
                    localest.append(msp(w)[e])
            local.append(localest)
        sun+=cds(s,0,q)*(-1)**(q)*(oper(BdInStr(local),n-1))
    return sun

l = [msp(input())]                                  #ввод бд например
n = len(l[0])                                       #1 2 3
for q in range(n - 1):                              #4 5 6
    l.append(msp(input()))                          #7 8 9
#print(l,BdInStr(l))                                 #пример ввода и шифрования
#print(msl(BdInStr(l)),msp(msl(BdInStr(l))[0]))      #пример дешифрования
print(oper(BdInStr(l),n))
input('нажмите для завершения')
#примеры
'''
2 -3 5
1 0 -4
2 1 -1
ответ 34
'''
'''
1 5 25
1 7 49
1 8 64
ответ 6
'''
