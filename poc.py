#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
from alchemyapi import AlchemyAPI
import json
import pyen
import twitter
__author__ = 'Athithyaa'
api = twitter.Api(
 consumer_key='uuS2NoVIptN1FWIGOra5pQsBT',
 consumer_secret='V4qZduqrJkuPK92gBg8thzJVqzkXtwUgsZH5jW0dGGgLPFyz39',
 access_token_key='126299805-5u3iBfwKJFewLnnrI8ca1nq8X4nneubnYlXBC4NM',
 access_token_secret='EtIQWdOREhdaVsks9VPK7qiQ5LLw8JGSd6hgBcEky8LCA'
 )

demo_text = 'Yesterday dumb Bob destroyed my fancy iPhone in beautiful Denver, Colorado. I guess I will have to head over to the Apple Store and buy a new one.'
alchemyapi = AlchemyAPI()
cummalative_score = 0
number_of_tweets = 0
results = api.GetUserTimeline(screen_name = "isstiaung",include_rts=False, count=50)
for status in results:
	print('Created at:'+status.created_at+'Message:'+status.text)
	message= status.text
	number_of_tweets = number_of_tweets + 1
	response = alchemyapi.sentiment('text', message)
	if response['status'] == 'OK':
		print('## Response Object ##')
		print('Type: ', response['docSentiment']['type'])
		
		if( response['docSentiment']['type'] == "neutral"):
			cummalative_score = cummalative_score + 0
		else:
			cummalative_score = cummalative_score + float(response['docSentiment']['score'])
			print('Score: ', response['docSentiment']['score'])
		#print('Type: ', response['docSentiment']['type'])
	else:
		print('Error in entity extraction column')
print('cummalative_score:',cummalative_score)
print('average score:',(cummalative_score/number_of_tweets))

	#en = pyen.Pyen("NLZFOCISYFUJULXXJ")
	#responseEcho = en.get('song/search', mood='happy', results='20', max_liveness='0.7', min_liveness='0.4')
#print(' ## Response Echo')
#print(responseEcho)


																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																												