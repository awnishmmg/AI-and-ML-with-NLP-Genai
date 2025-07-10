
import joblib
import os 

model_path = './model.pkl'

# Take user input 
input_text = input('Enter the Text:')
cleaned_text = input_text.strip()

if os.path.exists(model_path):
    model  = joblib.load(model_path)
    prediction_arr = model.predict([cleaned_text])
    prediction = prediction_arr[0]
    print(f'Prediction : {prediction}')
else:
    print('Model Not Found !!!')



