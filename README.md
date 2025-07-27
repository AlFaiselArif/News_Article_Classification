# 📰 Fake News Classification App


This is a machine learning project that detects whether a news article is **real** or **fake** using Natural Language Processing (NLP) and Logistic Regression. It uses a trained model with TF-IDF vectorization and is deployed using Streamlit.


## 🚀 Live Demo

Try it here:  
👉 [Fake News Classifier](https://newsarticleclassification-dwscabcvvfvdxez7xs24x6.streamlit.app/)

![image](https://github.com/user-attachments/assets/13d97970-2521-4e05-8d19-06525bfd8cfb)



## 📂 Dataset Used

This project uses the **Fake and Real News Dataset** from Kaggle:

- 📄 **Fake.csv** – News marked as fake
- 📄 **True.csv** – News marked as real

🔗 [Kaggle Dataset Link](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset?select=Fake.csv)

> ⚠️ These files are **not included in the repository** due to GitHub’s file size limits (>25MB).  
> You can download them manually from Kaggle or this shared cloud link:


## 🧠 How It Works

1. Text from each news article is **cleaned and preprocessed**.
2. Articles are transformed using **TF-IDF vectorization**.
3. A **Logistic Regression model** (with class balancing) is trained on the processed data.
4. In the app, users paste an article, and the model predicts whether it’s **Real or Fake**.


## ⚠️ Missing Files Explanation

| File         | Included in GitHub? | Why |
|--------------|----------------------|-----|
| `model.pkl`  | ✅ Yes               | Pretrained model file |
| `tfidf.pkl`  | ✅ Yes               | TF-IDF vectorizer used for predictions |
| `Fake.csv`   | ❌ No                | File too large (>25MB) |
| `True.csv`   | ❌ No                | File too large (>25MB) |

You do not need the CSV files to use the **app**, only for retraining the model.

---

## 🛠️ Run Locally

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
