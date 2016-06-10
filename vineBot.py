import os
import sys
import argparse
from random import randint

reload(sys)
sys.setdefaultencoding("utf-8")

import requests
import json



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('botID')

    args = parser.parse_args()
    
    botID = args.botID

    postBot(botID)


def randomVine():

  endpoint = 'https://api.vineapp.com/timelines/popular'
  r = requests.get(endpoint)
  response = r.json()
 
  randomNumber = randint(0,19)

  return(response['data']['records'][randomNumber]['permalinkUrl'])



def postBot(botID):

  vineLink = randomVine()
  endpoint = 'https://api.groupme.com/v3/bots/post'
  r = requests.post(endpoint,
		json.dumps({
  			'bot_id' : botID,
  			'text' : vineLink
		})
	)


if __name__ == '__main__':
    main()
    sys.exit(0)
