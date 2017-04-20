#-*- coding: utf-8 -*-
import json
import sys
import re

class TypeAnalyzer:
    def __init__(self):
        pass

    def questionType(self, dp):

# for ETRI
#        for eojeol in dp:
#            if eojeol["head"] == -1 and eojeol["label"] == "VNP": #e.g.: ...해전은 무엇인가?
#                qType = 1
#            elif eojeol["head"] == -1 and eojeol["label"] == "NP": #e.g.: ...해전? or ...무엇?
#                qType = 4
#            elif eojeol["head"] == -1 and eojeol["label"] == "VP": #e.g.: ...해전은 무엇인지 말해보시오
#                qType = 3
#            elif eojeol["head"] == -1 and eojeol["label"] == "NP_SBJ": #e.g.: ...해전은?
#                qType = 2
#            else:
#                qType = 4

# for ESPRESSO
        for eojeol in dp:
            if eojeol['id'] == eojeol['head'] and eojeol['label'] == "VNP":
                qType = 1
            elif eojeol['id'] == eojeol['head'] and eojeol['label'] == "NP":
                qType = 2
            elif eojeol['id'] == eojeol['head'] and eojeol['label'] == "VP":
                qType = 3
            else:
                qType = 2
        return qType
'''
        if qType == 4: #예: ...해전? or ...무엇? 에 대한 분류
            for eojeol in dp:
                if eojeol["head"] == -1:
                    head_id = eojeol["id"]
            for eojeol in dp:
                if eojeol["head"] == head_id and eojeol["label"] == "NP_SBJ": #예: ...해전은 무엇?
                    qType = 1
                elif not eojeol["head"] == head_id and eojeol["label"] == "NP_SBJ": #예: ...지휘한 해전?
                    qType = 2
'''
#        return qType
