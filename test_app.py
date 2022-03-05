import time

import requests
from flask import Flask, request
from flask_restful import Resource, Api

from backend.model import toxicity_scores
from web.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200


def test_toxicity():
    app = Flask(__name__)
    api = Api(app)

    class HelloWorld(Resource):
        def get(self):
            sentence = request.args.get("data")
            toxicity = toxicity_scores(sentence)
            return {'sentence': sentence, 'toxicity': str(toxicity['toxicity']), 'severe_toxicity': str(toxicity['severe_toxicity']), 'obscene': str(toxicity['obscene']),
                    'threat': str(toxicity['threat']), 'insult': str(toxicity['insult']), 'identity_attack': str(toxicity['identity_attack'])}

    api.add_resource(HelloWorld, '/')
    client = app.test_client()

    url = '/?data=I%20hate%20everyone%20on%20this%20earth'
    response = client.get(url)
    assert response.get_data()


def test_connection():
    assert requests.get("http://localhost:5001").status_code == 200, "web site is not up"


def test_stress_requests():
    start = time.time()
    for i in range(1000):
        requests.get("http://localhost:5001")

    end = time.time() - start
    assert (end / 1000) < 100, "stress not passed"