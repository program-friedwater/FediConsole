import requests
from Fire import Fire
import uuid
login = 0
instances = 0
miauthuuid = 0
mitoken = 0
miaurl = 0
def login():      
    if login == 'Misskey':
        if instances == 0:
            instances = input("Please enter instances url.")
    else:
        if login == 'Mastodon':
            if instances == 0:
             instances = input("Please enter instances url.")
        else:
            snssetup()

def snssetup():
    login = input("Please enter SNS name.")
    instance = input("Please enter instances url.")
# ここからMisskey機能実装
def miauth():
    miauthuuid = uuid.uuid4()
    miaurl = "https://" + instances + "/" + miauthuuid + "/"

def mipost():
    login() # 適当に置いた