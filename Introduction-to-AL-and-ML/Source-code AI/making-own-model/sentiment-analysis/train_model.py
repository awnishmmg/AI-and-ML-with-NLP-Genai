import pandas as pd 
import joblib #train

#sklearn 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

#Baye' Theoram Classificiar
from sklearn.naive_bayes import MultinomialNB
#Making Model Workflow | Ml Pipelines | mlflow
from sklearn.pipeline import make_pipeline


# Prepare the data set -> mapping text(message) with labels


#dataframe 
df = pd.DataFrame(data_set)
#Encoding Techniques for the classfication 
#Labels Encode 
df['label'] = df['label'].astype('category')

#split and test the data and train 
X_train,X_test,y_train,y_test = train_test_split(df['text'],df['label'],test_size=0.2) #80,20 Rule

# Make the pipelines 
model = make_pipeline(CountVectorizer(),MultinomialNB())
# curvefitting 
model.fit(X_train,y_train)

if joblib.dump(model,'model.pkl'):
    print('Model Trained and Saved')




























