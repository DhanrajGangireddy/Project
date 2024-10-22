# Project
### Problem Statement
- Phishing attacks are a major threat to online security, often mimicking legitimate websites to steal sensitive information.
- Traditional security measures frequently fail to accurately identify phishing sites.
- This project uses Logistic Regression and TF-IDF Vectorization to classify URLs as either phishing or legitimate.
- The aim is to provide a robust and efficient method to detect phishing websites, enhancing overall cybersecurity defenses.

### Solution

- Data Collection: Gather a dataset of URLs labeled as phishing or legitimate.
- Preprocessing: Clean and preprocess the URLs to prepare them for vectorization.
- Feature Extraction: Use TF-IDF Vectorization to transform URL text data into numerical features.
- Data Scaling: Apply Standard Scaler to normalize the input features for better model performance.
- Model Training: Train a Logistic Regression model on the scaled and vectorized features to learn patterns indicative of phishing and legitimate sites.
- Evaluation: Achieved an accuracy of 93% with the test data using metrics such as accuracy, precision, recall, and F1 score.
- Deployment: Implemented a web application interface using Streamlit and deployed it on Hugging Face for real-time phishing URL detection.
  
Install Necessary Libraries
Run Command:
>>>>   streamlit run app.py
