# -*- coding: utf-8 -*-
from SPARQLWrapper import SPARQLWrapper, JSON
from nluEngines import requestService


def kbSPARQL(soc, qproperty):
    soc = soc.replace(' ','_')
    sparql = SPARQLWrapper("http://ko.dbpedia.org/sparql")
    sparql.setQuery("""
                    SELECT ?o WHERE {
                    dbpedia-ko:"""+soc+""" prop-ko:"""+qproperty+""" ?o .
                   }
                    """)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    answers = []
    if result['results']['bindings']:
        for i in result['results']['bindings']:
            answer = {}
            a = i['o']['value']
            a = a.replace('http://ko.dbpedia.org/resource/','')
            answer['name'] = a
            answer['score'] = 1
            #answer scoring
            answers.append(answer)
    return answers


def socSPARQL(entity):
    entity = entity.replace(' ','_')
    sparql = SPARQLWrapper("http://ko.dbpedia.org/sparql")
    sparql.setQuery("""
                    SELECT ?p ?o WHERE {
                    dbpedia-ko:"""+entity+""" ?p ?o .
                   }
                    """)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()

#    print("ENTITYLINKING: ",result['results']['bindings'])
    socList = []
    words = entity.split('_')
    if result['results']['bindings']:
        socList = result['results']['bindings']
    elif len(words) > 1:
        last_word = words[-1]
#        print("last_word: ",last_word)
        sparql.setQuery("""
                        SELECT ?p ?o WHERE {
                        dbpedia-ko:"""+last_word+""" ?p ?o .
                       }
                        """)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        socList = result['results']['bindings']
    else:
        pass
    return result['results']['bindings']

def qpSPARQL(soc, nextAction):
    soc = soc.replace(' ','_')
    sparql =SPARQLWrapper("http://ko.dbpedia.org/sparql")
    qfocus = nextAction['semanticContents']['qfocus']
    qverb = nextAction['semanticContents']['contents'][0]['qverb']
#    print("qfocus:",qfocus,"qverb:",qverb)
#    print("qverb: ",qverb)
    stemmer = requestService.Stemmer()
    stem = stemmer.stemming(qverb)
    qproperty = []
    while True:
        sparql.setQuery("""
                        SELECT ?p WHERE {
                        dbpedia-ko:"""+soc+""" ?p ?o .
                        FILTER(regex(?p, \'"""+qverb+"""\'))
                       }
                        """)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        if result['results']['bindings']:
            for i in result['results']['bindings']:
                qproperty.append(i)
        else:
            pass

        sparql.setQuery("""
                        SELECT ?p WHERE {
                        dbpedia-ko:"""+soc+""" ?p ?o .
                        FILTER(regex(?p, \'"""+qfocus+"""\'))
                        }
                        """)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        if result['results']['bindings']:
            for i in result['results']['bindings']:
                qproperty.append(i)
        else:
            pass
        if not result['results']['bindings']:
            print("Olivia>> OoV (Out of vocabulary) ...")
            sparql.setQuery("""
                            SELECT ?p WHERE {
                            dbpedia-ko:"""+soc+""" ?p ?o .
                            FILTER(regex(?p, 'property'))
                            }
                            """)
            sparql.setReturnFormat(JSON)
            result = sparql.query().convert()
            if result['results']['bindings']:
                for i in result['results']['bindings']:
                    qproperty.append(i)
            else:
                pass
        break

    return qproperty


