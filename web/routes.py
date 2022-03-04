import requests
from flask import request, render_template

import time, random

def configure_routes(app):
    @app.route('/')
    def form():
        return render_template('index.html')

    @app.route('/', methods=['POST'])
    def analyse():
        text_to_analyse = request.form['text']
        api_url = "http://api-toxicity:5001/?data=" + text_to_analyse
        response = requests.get(api_url)
        json_response = response.json()
        return render_template('index.html', final=True, toxicity = json_response['toxicity'], severe_toxicity = json_response['severe_toxicity'],
         obscene = json_response['obscene'], threat = json_response['threat'], insult = json_response['insult'], identity = json_response['identity_attack'])



