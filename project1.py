import streamlit as st
import nltk
import spacy
import string
import pandas as Pd 
import matplotlib.pyplot as plt

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer
from sklearn.feature_extraction.text import CountVectorizer


#download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

#load spacy model
nlp = spacy.load("en_core_web_sm")

#STREAMLIT PAGE CONFIGURATION
st.set_page_config(page_title="NLP Preprocessing", layout="wide")

#APP TITLE
st.title("NLP Preprocessing Application")
st.write("Tokenization, Stemming, Lemmatization,Text Cleaning ,Bag of words ")

#USER INPUT
text = st.text_area("Enter text for NLP preprocessing",height=150, placeholder="Example: Aman is the HOD of HIT  and loves NLP")

#SIBEBAR OPTIONS
st.sidebar.title("Preprocessing Options")
option = st.sidebar.radio("Select NLP Technique", ["Tokenization" , "Stemming", "Lemmatization", "Text Cleaning", "Bag of Words"])
#process button
if st.button("Process Text"):
    if text.strip() =="":
        st.warning("Please enter some text to process.")

#TOKENIZATION
    elif option == "Tokenization":
        st.subheader("Tokenization output")
        col1, col2 = st.columns(3)

        #sentence Tokenization
        with col1:
            st.markdko=wn("#### Sentence Tokenization")
            sentences = sent_tokenize(text)
            st.write(sentences)

            #word Tokenization
        with col2:
            st.markdown("#### Word Tokenization")
            words = word_tokenize(text)
            st.write(words)

            #character Tokenization
        with col3:
            st.markdown("#### Character Tokenization")
            characters = list(text)
            st.write(characters)

        #text cleaning
    elif option == "Text Cleaning":
        st.subheader("Text Cleaning Output")
        
        #convert text to lowercase
        text_lower = text.lower()

        #Remove punctuation & number 
        cleaned_text ="".join(ch for ch in text_lower if ch not in string.punctuation and not ch.isdigit())

        #Remove stopwords using spacy
        doc = nlp(cleaned_text)
        final_words = [token.text for token in doc if not token.is_stop and token.text.strip() != ""]

        st.markdown("### Original Text")
        st.write(text)

        st.markdown("### Cleaned Text")
        st.write(" ".join(final_words))

    #STEMMING
    elif option == "Stemming":
        st.subheader("Stemming Output")
        col1, col2 = st.columns(2)

        porter = PorterStemmer()
        lancaster = LancasterStemmer()

        #apply steamming
        porter_stems = [porter.stem(word) for word in words]
        lancaster_stems = [lancaster.stem(word) for word in words]
        

