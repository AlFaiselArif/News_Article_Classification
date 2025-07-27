import streamlit as st
import joblib
import os
import nltk

nltk.download('stopwords')

# Load model and vectorizer
if not os.path.exists("model.pkl") or not os.path.exists("tfidf.pkl"):
    st.error("⚠️ 'model.pkl' or 'tfidf.pkl' not found. Please run train_model.py first.")
else:
    model = joblib.load("model.pkl")
    vectorizer = joblib.load("tfidf.pkl")

    st.title("📰 Fake News Classifier")
    st.markdown("Enter a news article below to check whether it's **Real or Fake**.")

    news_text = st.text_area("Paste News Article Content Here", height=300)

    if st.button("Predict"):
        if news_text.strip() == "":
            st.warning("Please enter news content.")
        else:
            cleaned = news_text.lower()
            cleaned = ''.join([char for char in cleaned if char.isalpha() or char.isspace()])
            transformed = vectorizer.transform([cleaned])
            prediction = model.predict(transformed)[0]
            proba = model.predict_proba(transformed)[0][prediction]

            label = "✅ Real News" if prediction == 1 else "❌ Fake News"
            st.subheader(f"{label} (Confidence: {proba*100:.2f}%)")
