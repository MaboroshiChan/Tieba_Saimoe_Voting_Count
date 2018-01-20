import BDTB
import Count
import Tool
import urllib.request
import re

datas =[]
for i in range(1,19):

    BaseUrl = 'https://tieba.baidu.com/p/5475081737'
    bdtb = BDTB(BaseUrl, 0)
    G = bdtb.getPage(i)
    temp = bdtb.getContent(G)
    datas += list(temp)
F = open('Contests.txt', encoding='utf-8')
A = F.read()


Example = Count(raw=A, data=datas)

Cont = Count.CountCont(self=Example)
vote = Count.getCont(self=Example,Cont=Cont)
vote = Count.start(self=Example,vote=vote)
result = Count.result(self=Example,Cont=Cont, vote=vote)


print(result)

