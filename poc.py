from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import pyen

__author__ = 'Athithyaa'

demo_text = 'Yesterday dumb Bob destroyed my fancy iPhone in beautiful Denver, Colorado. I guess I will have to head over to the Apple Store and buy a new one.'
alchemyapi = AlchemyAPI()
response = alchemyapi.sentiment('text', demo_text)

if response['status'] == 'OK':
     print('## Response Object ##')
     print('Score: ', response['docSentiment']['score'])
     print('Type: ', response['docSentiment']['type'])
else:
     print('Error in entity extraction call: ', response['statusInfo'])

en = pyen.Pyen("NLZFOCISYFUJULXXJ")
responseEcho = en.get('song/search', mood='happy', results='20', max_liveness='0.7', min_liveness='0.4')
print(' ## Response Echo')
print(responseEcho)
