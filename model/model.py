from detoxify import Detoxify

def toxicity_scores(text):

    try:
        results = Detoxify('original').predict(text)

        return results
    except:
        return 'error'
    