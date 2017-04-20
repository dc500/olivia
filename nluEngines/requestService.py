#-*- coding: utf-8 -*-
import json
import urllib.request
import requests
import re
import xmlrpc.client

#사용법
#main 함수에
#parser = requestService.Parser()
#espresso = parser.espresso(text)

class Parser:
    def __init__(self):
        pass
    def etri(self, text):
#        url = "http://143.248.135.60:31235/etri_parser"
        url = "http://143.248.135.60:44416/etri_parser"
#        url = "http://143.248.135.20:22334/controller/service/etri_parser"
        values = {'text':text}
#        values = text.encode('utf-8')
        response = requests.post(url, data=values)
        result = response.text
        print("result: ",result)
        return result
    def espresso(self, text):
        server = xmlrpc.client.ServerProxy("http://wisekb.kaist.ac.kr:11111")
        nlp = server.parse(text)
        with open("./dummy.txt", "w") as f:
            f.write(nlp)
        with open("./dummy.txt", "r") as f:
            d = f.readlines()
        i = 0
        for line in d:
            if line.startswith("{"):
                jsonline = i
            i = i+1
        n = d[jsonline:]
        with open("./dummy.txt","w") as f:
            for i in n:
                f.write(i)

        with open("./dummy.txt", "r") as f:
            result = f.read()
        return result


class EntityLinking:
    def __init__(self):
        pass
    def elu(self, text):
        url = "http://143.248.135.60:2223/entity_full"
        values = {"text":text}
        response = requests.post(url, json=values)
        result = response.text
        return result


class Stemmer:
    def __init__(self):
#        print "...Loading Stemmer..."
        pass
    #입력 예: 해전/NNG+은/JX
    #출력 예: stem method: 해전 

    def stemming(self, text): #for ESPRESSO
#        parser = requestService.Parser()
        nlp = json.loads(Parser.espresso(self, text))
        morp = nlp['sentence'][0]['morp']
        stems = []
        affixes = [line.rstrip('\n') for line in open('./nluEngines/dictionary/KoreanAffixList.txt', 'r')]
        for m in morp:
            if m['type'] not in affixes:
                stems.append(m['lemma'])
            else:
                pass
        stem = ''.join(stems)
        return stem

    def stem(self, morp):
        morpWithPosTuple = re.split('[+]',morp) # + 단위로 tuple 생성 
        morpPosPairList = []
        morpList = []

        #stemming 시 지우는 POS tag 리스트 생성
        affixes = [line.rstrip('\n') for line in open('./nluEngines/dictionary/KoreanAffixList.txt', 'r')]

        for morpWithPos in morpWithPosTuple:
            morpPosPair = re.split('[/]',morpWithPos) # / 단위로 tuple 생성 후 리스트에 추가 (예: [(해전, NNG), (은, JX)]
            morpPosPairList.append(morpPosPair)

        for morpPosPair in morpPosPairList:
            if morpPosPair[1] not in affixes:
                morpList.append(morpPosPair[0])

        stem = ''.join(morpList) # stemming 된 형태소들을 합쳐줌. 예: "대한" "민국"


        for morpPosPair in morpPosPairList:
            if not morpPosPair[1] == affixes: # POS가 affixex가 아닐 경우
                morpList.append(morpPosPair[0]) # tuple 에서 POS를 제거

        return stem
        #return morpList
        #return morpPosPairList
        #return morpWithPosTuple

    def stemWithPos(self, morp):
        morpWithPosTuple = re.split('[+]',morp)
        morpPosPairList = []
        morpList = []
        affixes = ('JX')
        for morpWithPos in morpWithPosTuple:
            morpPosPair = re.split('[/]',morpWithPos)
            morpPosPairList.append(morpPosPair)

        for morpPosPair in morpPosPairList:
            if not morpPosPair[1] == affixes:
                morpList.append(morpPosPair[0])

        return morpList

class WSD:
    def __init__(self):
        pass
    def disambiguator(self, word, morp_id, wsd):
        for morp in wsd:
            if morp["begin"] == morp_id:
                posTag = morp["type"]
                scode = morp["scode"]
        wsdDict = {}
        wsdDict['text'] = word
        wsdDict['pos'] = posTag
        wsdDict['ws_code'] = scode

        return wsdDict

class remove:
    def dictInList(condition, yourlist):
        for k in xrange(len(yourlist)):
            if condition(yourlist[k]):
                del yourlist[k]
                break
        return yourlist



