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
        return a    #������� ũ�Ѹ�

    
class InOu:
    def Inp(self,a1):
        with open('sample.txt','w') as a:
            for i in a1:
                a.write(i)  #���� ���� ���� ����
        return
    def Oup(self):
        
        with open('sample.txt','r') as a:
            res=list()
            lines = a.readlines() #�ٷ� �ɰ���
            for i in lines:#�� �ٸ���
                ss=i.split() #�ܾ�� �ɰ���
                for k in ss: #�� �ܾ��
                    s1=k.lower() #�ҹ��� �ٲ۴�.
                    s2=re.sub('[\'(),-=.#/?:$}]','',s1) #Ư������ ����
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
        fi=sorted(di,key=di.get,reverse=True)  #���� �������� �����ϵ�, Ű�� �����ֱ� 
        print fi[:5]
    else:
        print 'unknown option'
        print 'c�Ǵ� h�Ǵ� t�� �Է��Ͻÿ�.'

if __name__=="__main__":
    ur = Cra("https://www.songtexte.com/songtext/freddie-mercury/bohemian-rhapsody-23982857.html")
    ree = ur.req()
    so = ur.soup(ree)
    song = ur.lyrics(so)  #������� ũ�Ѹ�
   
    inp = InOu()
    inp.Inp(song)  #���� ���� ���� ����

    ii = inp.Oup()   #�ܾ� ������ �߶� list�������� ��ȯ
    Cnt(ii)
    
    
    

    
