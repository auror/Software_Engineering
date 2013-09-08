from __future__ import division
import random
import math
import numpy
import pylab as pl

def func1(x):
    TPS = [['1','2','3','7'],['1','2','3','2','3','7'],['1','2','5','6','7'],['1','4','5','6','7'],['1','4','6','7']]
    
    x = [str(j) for j in x]
    count = 0
    for var1 in TPS:
        temp = x
        status = 0
        for var2 in var1:
            if var2 in temp:
                status = 1
                temp = temp[1+temp.index(var2):]
            else:
                status = 0
                break
        if status==1:
            count += 1
    return count/len(TPS)
            
def func2(x):
    CF = [10,6,6,3,1,1,4]
    total = 0
    for i in x:
        total += CF[i-1]
    return total

def Mut(x):
    length = len(x)
    rloop = random.randint(1,3)
    for i in range(0,rloop):
        rand = random.randint(0,length-1)
        rand1 = random.randint(1,7)
        x[rand] = rand1
    return x

def Cross(x,y):
    len1 = len(x)
    len2 = len(y)

    rand1 = random.randint(0,len1-1)
    rand2 = random.randint(0,len2-1)
    temp1 = x[0:rand1+1]
    temp2 = y[0:rand2+1]
    temp3 = x[rand1:]
    x = temp1 + y[rand2:]
    y = temp2 + temp3

    return [x,y]

def calculateP(pops):
    p = []
    for var in pops:
        p.append([func1(var),func2(var)])
    return p

def isValid(x):
    status = 0
    length = len(x)
    N = [[2,4],[3,5],[2,7],[5,6],[6],[7],[1]]
    for var in x:
        ind = x.index(var)
        if ind == length-1:
            break
        if x[ind+1] in N[var-1]:
            pass
        else:
            status = 1
            break
    if status==1:
        return False
    return True

def Generate(pops):
    children = []
    values = []
    height = len(pops)
    for var in pops:
        rand = random.randint(1,10)
        if rand>7:
            temp = Mut(var)
            if isValid(temp):
                children.append(temp)
        else:
            rand1 = random.randint(0,height-1)
            temp = pops[rand1]
            cross = Cross(var,temp)
            for var1 in cross:
                if isValid(var1):
                    children.append(var1)

    for var in children:
        if func1(var)==0.0:
            children.remove(var)
        else:
            temp = [func1(var),func2(var)]
            values.append(temp)
    return [children,values]


def NonDominatedSort(P):
    S = []
    length = len(P)
    for j in range(0,length):
        S.append([])
    n = [0]*length
    Front = []
    temp = []

    for p in P:
        for q in P:
            if p[0] >= q[0] and p[1] <= q[1]:
                S[P.index(p)].append(q)
            elif q[0] > p[0] and q[1] < p[1]:
                n[P.index(p)] += 1
            
        if n[P.index(p)] == 0:
            temp.append(p)

    Front.append(temp)

    i = 0
    while len(Front[i]) != 0:
        Q = []
        for p in Front[i]:
            for q in S[P.index(p)]:
                n[P.index(q)] -= 1

                if n[P.index(q)] == 0:
                    Q.append(q)

        i += 1
        Front.append(Q)

    Front.pop(-1)
    
    return Front


def CrowdingDistance(x,limit):
    count = 0
    status = 0
    need = []
    for var in x:
        if count+len(var)<=limit:
            count += len(var)
            need = need + var
        else:
            status = 1
            break
    if status ==1:
        temp = []
        temp1 = []
        for i in var:
            temp.append(i[0])
            temp1.append(i[1])
        mini = min(temp)
        ind = temp.index(mini)
        mini2 = temp1[ind]

    temp2 = []
    temp3 = []
    for j in var:
        dist = math.sqrt((j[0]-mini)**2 + (j[1]-mini2)**2)
        temp2.append(j)
        temp3.append(dist)
    temp3 = [int(yo) for yo in temp3]
    temp4 = temp3
        
    while count!=limit:
        elem = max(temp3)
        index = temp4.index(elem)
        need = need + [temp2[index]]
        temp3.remove(elem)
        count += 1
    return need

TestCase = [[1,2,3,2,5,6,7],[1,2,3,2,3,7,1,4,6,7],[1,4,5,6,7,1,4,6,7],[1,4,5,6,7,1,2,3,7],[1,4,5,6,7,1,2,3,2,3,7]]
P = [[func1(TestCase[0]),func2(TestCase[0])],[func1(TestCase[1]),func2(TestCase[1])],[func1(TestCase[2]),func2(TestCase[2])],[func1(TestCase[3]),func2(TestCase[3])],[func1(TestCase[4]),func2(TestCase[4])]]
Coverage = []
print 'Generation 0:'
print TestCase
i = 0
for i in range(0,7):
    print 'Generation ' + str(i) + ':'
    Children = Generate(TestCase)
    TestCase = TestCase + Children[0]
    print 'TestCases after reproduction:'
    print TestCase
    print '\n\n'
    P = P + Children[1]
    front = NonDominatedSort(P)
    yo = 0
    haha = 1
    for var in front:
        print 'Front ' + str(front.index(var)) + ':'
        for var1 in var:
            print TestCase[P.index(var1)]
            yo = yo + (var1[0]*100)
            haha += 1
    lite = yo/haha
    Coverage.append(lite)
    print'______________________________________________________________________'
    if lite>80:
        break
    #i+=1

res = CrowdingDistance(front,15)
tot = 0
top = 0
for k in res:
    c = int(k[0]*100)
    tot = tot + c
    if c>top:
        top = c
        ans = k
tot = tot/len(res)

print 'Average Coverage : ' + str(tot)
print 'Maximum Coverage : ' + str(top) + ' for TestCase : ' + str(TestCase[P.index(ans)])
axis = []
for i in range(1,len(Coverage)+1):
    axis.append(i)
pl.plot(axis,Coverage)
pl.show()
raw_input('Press<Enter>')
