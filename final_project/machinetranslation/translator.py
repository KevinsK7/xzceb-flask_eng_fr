from deep_translator import PonsTranslator

def englishToFrench(englishText):
    translator = PonsTranslator(source='en', target='fr')
    return translator.translate(englishText)

def frenchToEnglish(frenchText):
    translator = PonsTranslator(source='fr', target='en')
    return translator.translate(frenchText).replace(" hello", "")
