# -*- coding: utf-8 -*-
import json
import checkQuestion
import nlu
import nlg
import talkingAbout
import dialogueManager
import checkQuestion

class QAEngines:
    def __init__(self):
        pass

    def controller(self, utterance, utype):
        # 1. NLU 수행
        nluParserResult = nlu.nluParser(utterance)

        # 2. DA generation 수행
        nluResult = nlu.daGenerator(nluParserResult)

        # 3. nextAction()
        nextAction = dialogueManager.nextAction(nluResult)
        # 4. slotFilling
        entity, slotFilling = dialogueManager.slotFilling(nextAction)
        # 정답 말하는 단계에서 되묻기 (미래의 일) 
#        nextAction['dialogueAct'] = "answer"
#        print(nextAction)

        # 5. NLG
        response = nlg.simpleNLG(entity, slotFilling)

        # return nlg
        return response


#        nluResult = nlu.QAparser(utterance)

#        if utterance['topic'] == "undefined":
#            utterance = talkingAbout.topicIdentifier(utterance)

        response = utterance

        return response



    def nlgEngine(self, slotFillingResult):
        # hard-coded result
        with open("./outputExample.txt", encoding="utf-8") as f:
            response = json.load(f)
        return response
