import requests
import json
from Fire import Fire
import uuid
login = 0
instances = 0
miauthuuid = 0
mitoken = 0
miaurl = 0
okay = 0
vertkt = {"a" : "asdf"}
class fire:
    def snssetup():
        login = input("Please enter SNS name.")
        instance = input("Please enter instances url.")

    def login():      
        if login == 'Misskey':
            miauth()
        else:
            if login == 'Mastodon':
             instances = input("Please enter instances url.")
            else:
                snssetup()

# ここからMisskey機能実装
    def miauth():
        miauthuuid = uuid.uuid4()
        miaurl = "https://" + instances + "/" + miauthuuid + "/"
        response = requests.post(miaurl, json=vertkt)
        okay = input("ACCESS HERE" + miaurl)
        response_dict = json.loads(response.text)
        mktkn = response_dict["i"]

    def mipost():
        login() # 適当に置いた

if __name__ == '__main__':
    fire.Fire(fire)