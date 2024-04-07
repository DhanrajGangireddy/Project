import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler

def makeTokens(f):
    delimiters = ['//', '.', 'http']
    total_tokens = []
    for delimiter in delimiters:
        f = f.replace(delimiter, ' ')
    tokens = f.split()

    total_tokens = list(set(tokens))
    if 'com' in total_tokens:
        total_tokens.remove('com')
    if 'www' in total_tokens:
        total_tokens.remove('www')    

    return total_tokens

logit_model = joblib.load('logistic_regression_model.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
scaler = joblib.load('standard_scaler.pkl')


def predict(url):
    X = tfidf_vectorizer.transform([url])
    X_test = scaler.transform(X)
    prediction = logit_model.predict(X_test)
    return prediction[0]

# Streamlit UI
st.title('URL Safety Predictor')
st.write('Enter a URL below to check its safety:')
url_input = st.text_input('URL:', '')

if st.button('Predict'):
    if url_input:
        prediction = predict(url_input)
        result = 'Safe site' if prediction == 0 else 'Phishing site '
        st.write('Prediction:', result)
    else:
        st.write('Please enter a URL.')