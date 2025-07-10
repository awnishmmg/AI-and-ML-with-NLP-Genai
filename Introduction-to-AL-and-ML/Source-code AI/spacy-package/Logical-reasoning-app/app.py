import streamlit as st
import gensim.downloader as api
import matplotlib.pyplot as plt
from config import getModelBySize
import os

from helpers.RelationshipSolver import RelationshipSolver
from helpers.SimilarWords import SimilarWords
from helpers.OddOneOut import OddOneOut

st.title('Logical GPT')
st.write('Your own Logical GPT App to resolve the Logical Reasoning.')

st.session_state['status'] = 'local'

@st.cache_resource
def load_model(): #1.68 Gb : 300 Millions Pre-trained Models
    if os.path.exists('./models/google_word2vec_model.kv'):
        from gensim.models import KeyedVectors
        model = KeyedVectors.load('./models/google_word2vec_model.kv')
        st.session_state['status'] = 'local'
        return model
    else:
        model = api.load(getModelBySize(model_name='google_news',type='max'))
        model.save('./models/google_word2vec_model.kv') #key vectors
        st.session_state['status'] = 'server'
        return model

# Model is loaded
model = load_model()
if model:
    st.success(f'Model Loaded successfully from {st.session_state['status']}')   
    st.markdown('we can use this Model to solve different reasoning question')
     
    #save the model
    #model.save('my_google_model.model')

tabbed_ui = ['Relation Solver','Similar Words','Odd one out']
tab1,tab2,tab3 =  st.tabs(tabbed_ui)

#Relation Solver
with tab1:
    rs = RelationshipSolver(st=st,title='Relationship Solver',model=model)
    rs.render()

#Relation Solver
with tab2:
    sw = SimilarWords(st=st,title='Similar Words',model=model)
    sw.render() 
    # collect the words and vector scores.
    words = sw.getWords()
    scores = sw.getScores()
    word = sw.getOriginalWord()

    print(f' words : {words} and score : {scores}')

    # #Draw the Graph
    fig,axis = plt.subplots()

    axis.bar(words,scores,color='aqua')
    axis.set_title(f"Top Words Similar to '{word}'")
    axis.set_ylabel('Consine Similarity')
    axis.grid(True)
    #Rotate the Axis 
    axis.set_xticks(range(len(words)))
    axis.set_xticklabels(words,rotation=30,ha='right')
    #To Get the Streamlite Object
    st = sw.getSt()
    st.pyplot(fig)

with tab3:
    odd = OddOneOut(st=st,title='Find Odd One Out',model=model)
    odd.render()
