# -*- coding: utf-8 -*-
# FRDF-driven NLU parser
import json
from nluEngines import requestService, questionTypeAnalyzer, srlbased

def nluParser(utterance):
    parser = requestService.Parser()
#    nlpResult = json.loads(parser.etri(utterance['utterance'])) #etri parser, April, 2016
    nlp = json.loads(parser.espresso(utterance['utterance'])) #espresso parser, 2016
    nlpResult = nlp['sentence']
#    print(nlpResult[0])

    dp = nlpResult[0]["dependency"] # dependency parse
    srl = nlpResult[0]["SRL"] # semantic role labeling
#    morp = nlpResult[0]["morp_eval"] # morphological analysis
    morp = nlpResult[0]["morp"] # for morpheme ID
    word = nlpResult[0]["word"] # for eojeol ID
#    wsd = nlpResult[0]["WSD"] # word sense disambiguation


    # qFocus
    qnlu = srlbased.Parser()
    qFocus = qnlu.qFocusIdentifier(dp)
#    print("qFocus: ", qFocus)
    utterance['qfocus'] = qFocus
#    print(srl)
    contents = qnlu.contentsIdentifier(dp, srl)
    utterance['contents'] = contents
    utterance['answer'] = [{"name":"?x","score":0}]

    return utterance

def daGenerator(nluResult):
    if "?" in nluResult['utterance']:
        da = "setQuestion"
    elif nluResult['utterance'] == "맞아":
        da = "confirm"
    elif nluResult['utterance'] == "아니야":
        da = "disconfirm"
    else:
        da = "unknown"
    nluEngineResult = {}
    nluEngineResult['dialogueAct'] = da
    nluEngineResult['semanticContents'] = nluResult

    return nluEngineResult
