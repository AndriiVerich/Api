import requests
from flask import Flask, request

import json

app = Flask(__name__)

def get_name(nickname):
    url = 'https://api.worldoftanks.eu/wot/account/list/?application_id=146590e6da27abee8503dcf96c43313e&search='+ nickname

    response = requests.get(url)
    data = response.json()
    account_id = data['data'][0]['account_id']

    return account_id

def get_data(id):
    url = 'https://api.worldoftanks.eu/wot/account/info/?application_id=146590e6da27abee8503dcf96c43313e&account_id='+ str(id)
    response = requests.get(url)
    print(response.text)

# id = get_name('xthat10')
# get_data(id)

@app.route('/', methods= ["POST"])
def process():
    print(request.json)
    return {'ok':True}

if __name__ == '__main__':

    app.run(use_reloader=False)
