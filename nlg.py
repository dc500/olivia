# -*- coding: utf-8 -*-
import json

def simpleNLG(entity, slotFillingResult):
    if slotFillingResult['dialogueAct'] == "answer":
        response = answerNLG(slotFillingResult)
    elif slotFillingResult['dialogueAct'] == "socOok":
        response = socOokNLG(entity)
    elif slotFillingResult['dialogueAct'] == "qpOok":
        response = qpOokNLG(entity, slotFillingResult)
    else:
        response = error(slotFillingResult)
    
    return response

def answerNLG(slotFillingResult):
    #현재는 answer candidate 에서 되묻는 기능이 없음
    answer = slotFillingResult['semanticContents']['answer'][0]['name']
    soc = slotFillingResult['semanticContents']['soc']
    qverb = slotFillingResult['semanticContents']['contents'][0]['qverb']
    qfocus = slotFillingResult['semanticContents']['qfocus']
    qproperty = slotFillingResult['semanticContents']['contents'][0]['qproperty']
    if qverb == "null":
        text = soc+"의 "+qfocus+"은 "+answer+"야"
    else:
        text = soc+"의 "+qproperty+"은 "+answer+"야"
    response = {"utterance": text}
    return response

def socOokNLG(entity):
    text = "미안해, 네가 말하는 "+entity+"에 대한 지식은 아직 갖고 있지 않아 (Out of Knowledge). 다른걸 물어봐줄래?"
    response = {"utterance": text}
    return response

def qpOokNLG(entity, slotFillingResult):
    qverb = slotFillingResult['semanticContents']['contents'][0]['qverb']
    qfocus = slotFillingResult['semanticContents']['qfocus']
    text = "미안해, "+entity+"의 "+qfocus+"에 대한 지식은 아직 갖고 있지 않아. 다른걸 물어봐>줄래?"
    response = {"utterance": text}
    return response

def error(slotFillingResult):
    text = "원인을 알 수 없는 잘못된 대화입니다"
    response = {"utterance": text}
    return response
