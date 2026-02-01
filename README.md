# NLP-Driven Resume Classification

## Problem Statement
Recruiters receive large volumes of resumes for multiple job roles. Manually screening and categorizing these resumes is time-consuming, inconsistent, and prone to bias.  
This project aims to **automate resume categorization** based on resume text using classical **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques.

---

## Methodology

The project follows a structured data science workflow:

### 1. Data Cleaning and Preprocessing
To standardize resume text, the following steps were applied:
- Removed URLs, punctuation, numbers, and extra whitespaces
- Converted text to lowercase
- Removed stopwords

### 2. Exploratory Data Analysis (EDA)
EDA was conducted to understand dataset characteristics:
- Analyzed class distribution across job categories
- Studied variability in resume length

**Insights:** The dataset contains noisy and overlapping categories, which directly impacts achievable model performance.

### 3. Feature Engineering
- Converted text data into numerical features using **TF-IDF vectorization**
- Used **unigram and bigram representations**
- Limited vocabulary size to reduce sparsity and noise

> TF-IDF was selected for its simplicity, interpretability, and strong baseline performance in text classification tasks.

### 4. Model Experiments
- Multiple machine learning models were evaluated and compared
- Increasing model complexity did **not improve performance**, indicating that **data quality and category overlap** are the primary limiting factors

### 5. Final Model Selection
**Linear Support Vector Machine (LinearSVC)** was chosen as the final model because:
- Consistently outperformed other models
- Generalized better on noisy and overlapping text data
- Commonly used in real-world NLP and resume screening systems

### 6. Error Analysis
- Most misclassifications occurred between **closely related roles**  
  e.g., DevOps Engineer resumes sometimes classified as Automation Testing  
- Reflects real-world role overlap rather than model instability  
- Indicates the model makes **logical and interpretable mistakes**

### 7. Deployment
- A **Streamlit web application** was developed for end-to-end demonstration
- Users can input resume text and receive **real-time job category predictions**
- Simulates a practical **automated resume screening workflow**

---

## Project Summary
This project demonstrates a **complete NLP pipeline for resume categorization**, combining:
- Careful **data preprocessing**
- Interpretable **feature engineering**
- Systematic **model evaluation**
- Practical **deployment** for real-world use

---

## Tools & Technologies
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, scikit-learn, NLTK, Streamlit  
- **Machine Learning Models:** LinearSVC, Random Forest, Logistic Regression (for comparison)  
- **Deployment:** Streamlit web app

---

## Usage
1. Clone the repository
2. Install required packages:
```bash
pip install -r requirements.txt
