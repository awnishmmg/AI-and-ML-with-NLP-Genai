

import numpy as np


def avg_word_2_vector(sentence,model):
    ''''
        @title : Average Custom Word2Vector
        @author : Awnish Kumar
        @version :1.0.1
        @license : MIT
        @description : This is Average Word2vector Vector function 
        which can take a pre-trained model and return the vector matrix as 
        per given sentence
        @parameter : <sentence>,<model>,<param?>
    '''
    words = sentence.lower().split() #convert to lower case and split using space
    word_vec = [model[word] for word in words if word in model]
    return np.mean(word_vec,axis=0) if word_vec else np.zeros(model.vector_size)


def __version__():
    return '1.1.0'

def init():
    print('imported success')