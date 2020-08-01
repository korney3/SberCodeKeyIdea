import pandas as pd
import os
from tqdm import tqdm
import json

KEYWORDS_PATH = '../Resources'

DATA_PATH = '../Resources'

MODEL_PATH = '../'

def FLAIR_MODEL(text):

    with open(os.path.join(KEYWORDS_PATH,'team_keywords.json'),'r') as f:
        team_names_keywords = json.load(f)

    with open(os.path.join(KEYWORDS_PATH,'grouped_team_keywords.json'),'r') as f:
        groups_keywords = json.load(f)

    team_names_keywords_vects = [' '.join(team_names_keywords[team]) for team in team_names_keywords]
#     group_names_keywords_vects = [' '.join(groups_keywords[team]) for team in groups_keywords]
    
    

    from flair.embeddings import WordEmbeddings, DocumentPoolEmbeddings
    from flair.data import Sentence
    
    from collections import OrderedDict


    
    from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity


    # initialize the word embeddings
    glove_embedding = WordEmbeddings(os.path.join(MODEL_PATH, 'ru-wiki-fasttext-300d-1M'))

    # initialize the document embeddings, mode = mean
    document_embeddings = DocumentPoolEmbeddings([glove_embedding])
    
    import string
    def text_embeddings(text):
        sentence = Sentence(text)
        document_embeddings.embed(sentence)
        return sentence.embedding.numpy()
    
    text_vec = text_embeddings(text)
    
    teams_vecs = []
    for team in tqdm(team_names_keywords_vects):
        teams_vecs.append(text_embeddings(team))
    
    predictions = {}
    destinations = {}
    for i,team in enumerate(teams_vecs):
        dest = euclidean_distances([text_vec], [team])[0]
        destinations[list(team_names_keywords.keys())[i]] = dest
    scores = OrderedDict(sorted(destinations.items(), key=lambda kv: kv[1]))
    predictions['euclid_team'] = list(scores.keys())[0]
    predictions['euclid_score'] = scores[list(scores.keys())[0]][0]

    
    destinations = {}
    for i,team in enumerate(teams_vecs):
        dest = cosine_similarity([text_vec], [team])[0]
        destinations[list(team_names_keywords.keys())[i]] = dest
    scores = OrderedDict(sorted(destinations.items(), key=lambda kv: kv[1],reverse=True))
    predictions['cosine_team'] = list(scores.keys())[0]
    predictions['cosine_score'] = scores[list(scores.keys())[0]][0]
    predictions['text'] = text
    
    return predictions

def BERT_MODEL(text):

    with open(os.path.join(KEYWORDS_PATH,'team_keywords.json'),'r') as f:
        team_names_keywords = json.load(f)

    with open(os.path.join(KEYWORDS_PATH,'grouped_team_keywords.json'),'r') as f:
        groups_keywords = json.load(f)

    team_names_keywords_vects = [' '.join(team_names_keywords[team]) for team in team_names_keywords]
#     group_names_keywords_vects = [' '.join(groups_keywords[team]) for team in groups_keywords]
    
    

    from sentence_transformers import SentenceTransformer, util
    
    from collections import OrderedDict


    
    from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity


    # initialize the word embeddings
    embedder = SentenceTransformer(os.path.join(MODEL_PATH,'public.ukp.informatik.tu-darmstadt.de_reimers_sentence-transformers_v0.2_distiluse-base-multilingual-cased.zip'))

    # initialize the document embeddings, mode = mean
    teams_vecs = embedder.encode(team_names_keywords_vects)


    
    text_vec = embedder.encode(text)[0]
    
    predictions = {}
    destinations = {}
    for i,team in enumerate(teams_vecs):
        dest = euclidean_distances([text_vec], [team])[0]
        destinations[list(team_names_keywords.keys())[i]] = dest
    scores = OrderedDict(sorted(destinations.items(), key=lambda kv: kv[1]))
    predictions['euclid_team'] = list(scores.keys())[0]
    predictions['euclid_score'] = scores[list(scores.keys())[0]][0]

    
    destinations = {}
    for i,team in enumerate(teams_vecs):
        dest = cosine_similarity([text_vec], [team])[0]
        destinations[list(team_names_keywords.keys())[i]] = dest
    scores = OrderedDict(sorted(destinations.items(), key=lambda kv: kv[1],reverse=True))
    predictions['cosine_team'] = list(scores.keys())[0]
    predictions['cosine_score'] = scores[list(scores.keys())[0]][0]
    predictions['text'] = text
    
    return predictions