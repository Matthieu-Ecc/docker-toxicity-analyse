from detoxify import Detoxify

def toxicity_scores(text):

    results = Detoxify('original').predict(text)

    return results
    