# -*- coding: utf-8 -*-
# talkingAbout() module
import json
import checkQuestion
import requests
from nluEngines import requestService

def topicIdentifier(text):
    entityLinking = requestService.EntityLinking()
    entities = entityLinking.elu(text)

    return entities
