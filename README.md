# Sentiment Analysis on Nykaa Beauty Product Reviews

## 📌 Project Overview
This project performs **sentiment analysis on real-world beauty product reviews** collected from the Nykaa e-commerce platform. The goal is to understand customer opinions and compare how different classical machine learning models perform on text data.

The project follows an **end-to-end applied ML workflow**: data collection → cleaning → labeling → feature extraction → model training → evaluation → visualization.

---

## 📊 Dataset Description
- **Source**: Nykaa product review pages (multiple beauty products)
- **Data type**: User-written textual reviews
- **Final dataset size**: ~100 reviews
- **Sentiment classes**:
  - `strong_positive`
  - `mixed_feedback`

This dataset is intentionally realistic and noisy, unlike clean benchmark datasets.

---

## 🛒 How Data Was Collected
- Nykaa product review pages were accessed manually in a browser.
- Due to anti-scraping restrictions (403 errors), pages were **saved as HTML files locally**.
- Reviews were extracted using **BeautifulSoup** by parsing relevant HTML tags.
- Multiple products were used to ensure **variety in opinions** and reduce bias.

✔ This approach respects website restrictions while still working with real data.

---

## 🧹 Data Cleaning Process
The raw scraped data contained:
- Duplicate reviews
- “Read More” truncation text
- Extra punctuation and casing inconsistencies

Cleaning steps:
- Removed duplicate reviews
- Removed UI text such as `...Read More`
- Converted text to lowercase
- Filtered very short/non-informative reviews

This ensured cleaner and more meaningful text for modeling.

---

## 🏷️ How Labeling Was Done
Manual rule-based labeling was applied:
- Reviews with clear praise, strong satisfaction → `strong_positive`
- Reviews with both pros and cons, neutral tone → `mixed_feedback`

Why not automated labeling?
- Dataset is small
- Manual labeling improves **label quality and interpretability**

This mimics real-world scenarios where domain knowledge matters.

---

## 🔤 Feature Extraction
Two vectorization techniques were used:

### 1️⃣ Count Vectorizer
- Converts text into word-frequency vectors
- Simple and effective for probabilistic models
- Used with Naive Bayes

### 2️⃣ TF-IDF Vectorizer
- Penalizes common words and boosts informative terms
- Reduces noise from frequently occurring words
- Used with Logistic Regression and Decision Tree

Using both allows comparison of **frequency-based vs importance-based representations**.

---

## 🤖 Models Used (and Why)

### ✅ Naive Bayes
- Works well with sparse, high-dimensional text data
- Fast and probabilistic
- Strong baseline for NLP tasks

### ✅ Logistic Regression
- Linear model with good generalization
- Handles TF-IDF features well
- Often outperforms more complex models on text

### ✅ Decision Tree
- Included for comparison
- Helps demonstrate why tree-based models often struggle with sparse text features

❌ Deep learning was avoided intentionally due to small dataset size.

---

## 📈 Model Evaluation Strategy
Evaluation was done using:
- **Accuracy**
- **Precision, Recall, F1-score**
- **Confusion Matrix** (for error analysis)

Why confusion matrix?
- Accuracy alone can be misleading
- Shows which sentiment classes are being confused
- Helps identify overfitting (especially in Decision Trees)

---

## ⚠️ Challenges Faced
- Website scraping restrictions (403 errors)
- Managing Jupyter notebook execution order
- Class imbalance toward positive reviews
- Sparse dataset size limiting model complexity

These challenges reflect **real-world ML issues**, not textbook problems.

---

## 🚀 Possible Future Improvements
- Add neutral/negative sentiment by including low-rated products
- Use cross-validation instead of single split
- Experiment with bigrams/trigrams tuning
- Try word embeddings (Word2Vec, GloVe)
- Deploy as a simple web app for live predictions

---

## 🎯 Practical Use of This Project
- Understand customer sentiment trends
- Help brands analyze product feedback
- Identify mixed or borderline reviews
- Serve as a template for real-world NLP pipelines

---

## 🧠 Key Learnings
- Classical ML models are still very effective for NLP
- Feature engineering matters more than model complexity
- Proper evaluation is critical for trustworthy results

---

## 📎 Tech Stack
- Python
- Pandas, NumPy
- BeautifulSoup
- Scikit-learn
- Matplotlib

---

## 👤 Author
**Praveen Kumar**

---

⭐ If you found this project useful, feel free to fork or star the repository!

