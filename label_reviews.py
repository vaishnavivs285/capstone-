import pandas as pd

df = pd.read_csv("nykaa_reviews_clean.csv")

strong_positive_words = [
    "love", "amazing", "best", "perfect",
    "holy grail", "highly recommend",
    "flawless", "obsessed"
]

mixed_words = [
    "but", "however", "though", "although", "wish",
    "oxidize", "cakey", "heavy", "dry",
    "expensive", "could be better"
]

def label_sentiment(text):
    text = text.lower()

    strong_pos = sum(word in text for word in strong_positive_words)
    mixed = sum(word in text for word in mixed_words)

    if strong_pos > 0 and mixed == 0:
        return "strong_positive"
    else:
        return "mixed_feedback"

df["sentiment"] = df["review"].apply(label_sentiment)

print(df["sentiment"].value_counts())

df.to_csv("nykaa_reviews_labeled.csv", index=False)
