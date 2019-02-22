import requests
from bs4 import BeautifulSoup
import os
import re

class Cra:
    def __init__(self,url):
        self.url = url
    def req(self):
        r=requests.get(self.url)
        return r
    def soup(self,s):
        soup = BeautifulSoup(s.content,"html.parser")
        return soup
    def lyrics(self,a1):
        lyr = a1.find_all(id="lyrics")
        for i in lyr:
            a =i.get_text()
        return a    #여기까지 크롤링

    
class InOu:
    def Inp(self,a1):
        with open('sample.txt','w') as a:
            for i in a1:
                a.write(i)  #가사 담은 파일 생성
        return
    def Oup(self):
        
        with open('sample.txt','r') as a:
            res=list()
            lines = a.readlines() #줄로 쪼개서
            for i in lines:#각 줄마다
                ss=i.split() #단어로 쪼개고
                for k in ss: #각 단어마다
                    s1=k.lower() #소문자 바꾼다.
                    s2=re.sub('[\'(),-=.#/?:$}]','',s1) #특수문자 제거
                    res.append(s2)
        return res            


def Cnt(a):
    di=dict()
    for i in a:
        di[i]=a.count(i)
    k=di.keys()
    v=di.values()
    choice = raw_input()
    if choice == 'c':
        print di
    elif choice == 'h':
        for i in range(len(k)):
            print k[i]+':'+'*'*v[i]
    elif choice == 't':
        fi=sorted(di,key=di.get,reverse=True)  #값을 역순으로 정렬하되, 키를 보여주기 
        print fi[:5]
    else:
        print 'unknown option'
        print 'c또는 h또는 t를 입력하시오.'

if __name__=="__main__":
    ur = Cra("https://www.songtexte.com/songtext/freddie-mercury/bohemian-rhapsody-23982857.html")
    ree = ur.req()
    so = ur.soup(ree)
    song = ur.lyrics(so)  #여기까지 크롤링
   
    inp = InOu()
    inp.Inp(song)  #가사 담은 파일 생성

    ii = inp.Oup()   #단어 단위로 잘라서 list형식으로 반환
    Cnt(ii)
    
    
    

    
