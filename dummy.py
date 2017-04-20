# -*- coding: utf-8 -*-
import json
from nluEngines import requestService

parser = requestService.Parser()
espresso = json.loads(parser.espresso("안녕"))


print(espresso)
