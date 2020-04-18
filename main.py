import wikipedia

def hello_wikipedia(request):
    """Takes JSON Payload {"entity": "google"}
    """
    request_json = request.get_json()

    if request_json and 'entity' in request_json:
        entity = request_json['entity']
        print(entity)
        res = wikipedia.summary(entity, sentences=1)
        return res
    else:
        return f'No Payload'
