import wikipedia

from google.cloud import translate

def sample_translate_text(text="YOUR_TEXT_TO_TRANSLATE", project_id="YOUR_PROJECT_ID"):
    """Translating Text."""

    client = translate.TranslationServiceClient()

    parent = client.location_path(project_id, "global")

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type="text/plain",  # mime types: text/plain, text/html
        source_language_code="en-US",
        target_language_code="fr",
    )
    # Display the translation for each input text provided
    for translation in response.translations:
        print(u"Translated text: {}".format(translation.translated_text))
    return u"Translated text: {}".format(translation.translated_text)

def translate_test(request):
    """Takes JSON Payload {"entity": "google"}
    """
    request_json = request.get_json()

    if request_json and 'entity' in request_json:
        entity = request_json['entity']
        print(entity)
        res = wikipedia.summary(entity, sentences=1)
        trans=sample_translate_text(text=res, project_id="cloudai-194723")
        return trans
    else:
        return f'No Payload'
