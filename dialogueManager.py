# -*- coding: utf-8 -*-
import json
import checkQuestion
import kbInterface

def nextAction(nluResult):
    da = "answer"
    if nluResult['semanticContents']['soc'] == "undefined":
        da = "checkQuestion"
    else:
        for i in nluResult['semanticContents']['contents']:
            if i['qproperty'] == "undefined":
                da = "checkQuestion"
            else:
                pass
    nluResult['dialogueAct'] = da
    return nluResult

def slotFilling(nextAction):
    #entity 는 1개 있다고 가정
    qproperty = "undefined"
    for i in nextAction['semanticContents']['contents']:
        for a in i['arg']:
            if a['text'] is not '?x':
                entity = a['text']
                break
    slotFillingResult = nextAction

    if nextAction['dialogueAct'] == 'answer':
        kbinterface = "true" #한번에 답을 찾은 경우
    elif nextAction['dialogueAct'] == 'checkQuestion':
        while True:
            if nextAction['semanticContents']['soc'] == "undefined":
                soc = checkQuestion.socChecker(entity)
                if soc == "undefined":
                    slotFillingResult['dialogueAct'] = 'socOok'
                    break
                else:
                    slotFillingResult['semanticContents']['soc'] = soc
            else:
                pass
            for i in nextAction['semanticContents']['contents']:
                if i['qproperty'] == "undefined":
                    qproperty = checkQuestion.qpropertyChecker(soc, nextAction)
                    i['qproperty'] = qproperty
            if qproperty == "undefined":
                slotFillingResult['dialogueAct'] = 'qpOok'
                break
            else:
                slotFillingResult['dialogueAct'] = 'answer'
                break
        if slotFillingResult['dialogueAct'] == 'answer':
            answers = kbInterface.kbSPARQL(soc, qproperty)
            slotFillingResult['semanticContents']['answer'] = answers
        else:
            pass

    else:
        print("잘못된 대화입니다 ERROR")

    return entity,  slotFillingResult



#def slotFilling(nextAction):
#    if nextAction['dialogueAct'] == "answer":
#        Do_KBQA
#    else:
#        checking()
# entity linking --> AGDISTIS
# property linking --> translation --> property linking?
# or Korean verb-predicate mapping pairs
# KB interface --> 1. SPARQL directly, 2. OKBQA interface
# 질문에 ?이 있는 경우 --> qa // 질문에 ?가 없는 경우 --> chit-chat


