import requests
from Fire import Fire
login = 0
instances = 0
def app() :
    if login == 'Misskey':
        if instances == 0:
            instances = input("Please enter instances url.")
    else:
        if login == 'Mastodon':
            if instances == 0:
             instances = input("Please enter instances url.")
    else:
        login = input("Please enter SNS name.")
        
