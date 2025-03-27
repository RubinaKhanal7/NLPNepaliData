import streamlit as st
import pickle
import pandas as pd

st.title('Nepali News Category Classifier')

model = pickle.load(open('NepaliData.pickle', 'rb'))

news_text = st.text_area("Enter Nepali News Article", height=250)

if st.button('Predict Category'):
    if news_text.strip():
        df = pd.DataFrame({'news_text': [news_text]})  
        prediction = model.predict(df['news_text'])[0]  
        st.success(f"Predicted Category: {prediction}") 
    else:
        st.warning("Please enter some text") 
