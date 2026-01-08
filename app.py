#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import joblib
import re

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Resume Classification App",
    layout="centered"
)

# -------------------------------
# Load saved models
# -------------------------------
@st.cache_resource
def load_models():
    tfidf = joblib.load("models/tfidf_vectorizer.pkl")
    svm_model = joblib.load("models/linear_svm_model.pkl")
    label_encoder = joblib.load("models/label_encoder.pkl")
    return tfidf, svm_model, label_encoder

tfidf, svm_model, label_encoder = load_models()

# -------------------------------
# Text cleaning function
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("📄 Resume Classification")
st.write("Paste a resume below to predict its job category.")

resume_text = st.text_area(
    "Resume Text",
    height=300
)

if st.button("Predict Category"):
    if resume_text.strip() == "":
        st.warning("Please paste resume text.")
    else:
        cleaned_text = clean_text(resume_text)
        vectorized_text = tfidf.transform([cleaned_text])
        prediction = svm_model.predict(vectorized_text)
        predicted_category = label_encoder.inverse_transform(prediction)[0]

        st.success(f"✅ Predicted Category: **{predicted_category}**")

