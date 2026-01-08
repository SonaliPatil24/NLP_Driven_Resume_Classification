# NLP_Driven_Resume_Classification

**Problem Statement**

Recruiters receive large volumes of resumes for multiple job roles. Manually screening and categorizing these resumes is time-consuming, inconsistent, and prone to bias. This project aims to automate resume categorization based on resume text using classical natural language processing and machine learning techniques.

**Methodology**

1.The project follows a structured data science workflow.
2.Data Cleaning and Preprocessing

The following preprocessing steps were applied to standardize resume text:
1.Removed URLs, punctuation, numbers, and extra whitespaces
2.Converted text to lowercase
3.Removed stopwords



  **Exploratory Data Analysis**

Exploratory data analysis was conducted to understand the dataset characteristics:
1.Analyzed class distribution across job categories
2.Studied variability in resume length
EDA revealed that the dataset contains noisy and overlapping categories, which directly impacts achievable model performance.

  **Feature Engineering**

1.Text data was converted into numerical features using TF-IDF vectorization.
2.Used unigram and bigram representations
3.Limited vocabulary size to reduce sparsity and noise
TF-IDF was selected for its simplicity, interpretability, and strong baseline performance in text classification tasks.

**Model Experiments**
1.Multiple machine learning models were evaluated and compared.
Increasing model complexity did not improve performance. This indicates that data quality and category overlap, rather than algorithm selection, is the primary limiting factor.

**Final Model Selection**
Linear Support Vector Machine was selected as the final model because:
1.It consistently outperformed other models
2.It generalized better on noisy and overlapping text data
3.It is commonly used in real-world NLP and resume screening systems

   **Error Analysis**

Error analysis revealed that most misclassifications occurred between closely related roles. For example, resumes belonging to DevOps Engineers were sometimes classified as Automation Testing. These errors reflect real-world role overlap rather than model instability, indicating that the model makes logical mistakes.

  **Deployment**

A Streamlit web application was developed to demonstrate end-to-end usability. The application allows users to input resume text and receive real-time job category predictions, simulating an automated resume screening workflow.

  **Project Summary**

This project demonstrates a complete natural language processing pipeline for resume categorization, combining careful data preprocessing, interpretable feature engineering, systematic model evaluation, and practical deployment.
