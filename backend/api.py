from flask import Flask, request
from flask_restful import Resource, Api

from model import toxicity_scores

from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
api = Api(app)
metrics = PrometheusMetrics(app)

class HelloWorld(Resource):
    def get(self):
        sentence = request.args.get("data")
        toxicity = toxicity_scores(sentence)
        return {'sentence': sentence, 'toxicity': str(toxicity['toxicity']), 'severe_toxicity': str(toxicity['severe_toxicity']), 'obscene': str(toxicity['obscene']),
                'threat': str(toxicity['threat']), 'insult': str(toxicity['insult']), 'identity_attack': str(toxicity['identity_attack'])}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)