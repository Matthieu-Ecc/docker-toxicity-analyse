from flask import Flask, request
from flask_restful import Resource, Api

from model import toxicity_scores

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        sentence = request.args.get("data")
        toxicity = toxicity_scores(sentence)
        return {'sentence': sentence, 'toxicity': toxicity['toxicity'], 'severe toxicity': toxicity['severe_toxicity'], 'obscene': toxicity['obscene'],
                'threat': toxicity['threat'], 'insult':toxicity['insult'], 'identity_attack':toxicity['identity_attack']}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)