# -*- coding: utf-8 -*-
# CHECK QUESTION MODULE for 1) entitiy, and 2) property

import json
import requests
import kbInterface

def socChecker(entity):
    result = kbInterface.socSPARQL(entity)
    soc = "undefined"
    checking = "false"
    socCandidates = []
    if result:
        for i in result:
            if i['o']['value'] == "http://ko.dbpedia.org/resource/틀:동음이의":
                checking = "true"
            else:
                pass
    else:
        checking = "noentity"
#    print("checking: ",checking)
    if checking == "true":
        for i in result:
            if i['p']['value'] == "http://dbpedia.org/ontology/wikiPageDisambiguates":
                candidate = i['o']['value']
                candidate = candidate.replace('http://ko.dbpedia.org/resource/','')
                candidate = candidate.replace('_',' ')
                socCandidates.append(candidate)
            else:
                pass
        while True:
            for i in socCandidates:
                print("Olivia>> 너가 말한 "+entity+"가 "+i+"가 맞니? (응/아냐)")
                feedback = input("USER>> ")
                if feedback == "응":
                    soc = i
                    break
                else:
                    pass
            break
    elif checking == "false":
        soc = entity
    else:
        pass
        
    return soc


def qpropertyChecker(soc, nextAction):
    with open('./dict/propBlackList.txt','r') as f:
        blacklist = f.readlines()
    blacklist = [x.strip() for x in blacklist]
    soc = soc.replace('_',' ')
    propCandidates = []
    qproperty = "undefined"
    result = kbInterface.qpSPARQL(soc, nextAction)
    for i in result:
#        print("i: ",i)
        prop = i['p']['value']
        if prop.find("/property/"):
            propCandidate = prop
            prop = prop.replace('http://ko.dbpedia.org/property/','')
            if prop not in blacklist:
                propCandidates.append(prop)
        else:
            pass
    propCandidates = [i for n,i in enumerate(propCandidates) if i not in propCandidates[n+1:]]
    while True:
        if propCandidates:
            for i in propCandidates:
                print("Olivia>> "+soc+"의 "+i+"를 묻는거니? (응/아냐)")
                feedback = input("USER >> ")
                if feedback == "응":
                    qproperty = i
                    break
                else:
                    pass
            break
        else:
            break


    return qproperty
