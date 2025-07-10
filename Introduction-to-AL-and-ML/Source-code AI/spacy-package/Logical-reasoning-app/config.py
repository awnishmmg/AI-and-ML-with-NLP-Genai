
page_config = {
    'page_title' : 'Aptitude GPT',
    'layout':'centered'
}

MODELS = {
    'google_news' : {
        'min' : 'word2vec-google-news-50',
        'medium' : 'word2vec-google-news-100',
        'max' : 'word2vec-google-news-300'
                },
    'glove_twitter' :  {
        'min' : 'glove-twitter-25',
        'medium' : 'glove-twitter-100'
    },
    'glove_wiki' : {
        'min' : 'glove-wiki-gigaword-50',
        'medium' : 'glove-wiki-gigaword-100'
    }
}

def getModelBySize(model_name,type='min'):
    model_name = MODELS[model_name][type]
    print('finding the Modelname :',model_name)
    return model_name



