# NLP_Driven_Resume_Classification

Resume Categorization and Screening System
Problem Statement

Recruiters receive large volumes of resumes for multiple job roles. Manually screening and categorizing these resumes is time-consuming, inconsistent, and prone to bias. This project aims to automate resume categorization based on resume text using classical natural language processing and machine learning techniques.

Methodology

The project follows a structured data science workflow.

Data Cleaning and Preprocessing

The following preprocessing steps were applied to standardize resume text:

Removed URLs, punctuation, numbers, and extra whitespaces

Converted text to lowercase

Removed stopwords

Standardized resume text for modeling

Exploratory Data Analysis

Exploratory data analysis was conducted to understand the dataset characteristics:

Analyzed class distribution across job categories

Studied variability in resume length

Observed significant overlap between closely related roles such as DevOps Engineer and Automation Testing

EDA revealed that the dataset contains noisy and overlapping categories, which directly impacts achievable model performance.

Feature Engineering

Text data was converted into numerical features using TF-IDF vectorization.

Used unigram and bigram representations

Limited vocabulary size to reduce sparsity and noise

TF-IDF was selected for its simplicity, interpretability, and strong baseline performance in text classification tasks.

Model Experiments

Multiple machine learning models were evaluated and compared.

Increasing model complexity did not improve performance. This indicates that data quality and category overlap, rather than algorithm selection, is the primary limiting factor.

Final Model Selection

Linear Support Vector Machine was selected as the final model because:

It consistently outperformed other models

It generalized better on noisy and overlapping text data

It is commonly used in real-world NLP and resume screening systems

Error Analysis

Error analysis revealed that most misclassifications occurred between closely related roles. For example, resumes belonging to DevOps Engineers were sometimes classified as Automation Testing. These errors reflect real-world role overlap rather than model instability, indicating that the model makes logical mistakes.

Technology Stack

Python

Pandas and NumPy

Scikit-learn

TF-IDF Vectorization

Linear Support Vector Machine

Matplotlib and Seaborn

Streamlit

Deployment

A Streamlit web application was developed to demonstrate end-to-end usability. The application allows users to input resume text and receive real-time job category predictions, simulating an automated resume screening workflow.

Project Summary

This project demonstrates a complete natural language processing pipeline for resume categorization, combining careful data preprocessing, interpretable feature engineering, systematic model evaluation, and practical deployment.
