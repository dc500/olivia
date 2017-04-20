#-*- coding: utf-8 -*-

import json
import utteranceClassifier

class IOAdapter:
    def __init__(self):
        pass
    def inputWrapper(self, input_utterance):
        # emotion 을 입력으로 받을 때에 대한 처리도 필요함 (To do)
        utterance = {}
        utterance['utterance'] = input_utterance
        utterance['emotion'] = "neutral"
        utterance['soc'] = "undefined"
        return utterance 

    def outputWrapper(self, response):
        output_response = response['utterance']
        return output_response

class Classifier:
    def __init__(self):
        pass
    def uClassifier(self, input_utterance):
        utype = utteranceClassifier.classifier(input_utterance)
        return utype
