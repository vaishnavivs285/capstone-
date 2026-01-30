from bs4 import BeautifulSoup
import pandas as pd

# -----------------------------
# 1️⃣ HTML FILES (5 PRODUCTS)
# -----------------------------
html_files = [
    "mac_reviews.html",
    "kay_lipstiick.html",
    "clinique_foundation.html",
    "eyeshadow.html",
    "c_lipstick.html"
]

all_reviews = []

# -----------------------------
# 2️⃣ LOAD + EXTRACT REVIEWS
# -----------------------------
for file_name in html_files:
    print(f"\nLoading {file_name}...")

    with open(file_name, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "html.parser")

    for tag in soup.find_all("p"):
        text = tag.get_text(strip=True)
        if len(text) > 30:
            all_reviews.append(text)

print("\nTotal raw reviews found:", len(all_reviews))

# -----------------------------
# 3️⃣ CLEAN + REMOVE NEAR DUPLICATES
# -----------------------------
cleaned_reviews = []
seen_keys = set()

for r in all_reviews:
    r = r.replace("...Read More", "")
    r = r.replace("...", "")
    r = r.lower().strip()

    if len(r) < 30:
        continue

    # fingerprint using first 12 words
    words = r.split()
    key = " ".join(words[:12])

    if key not in seen_keys:
        cleaned_reviews.append(r)
        seen_keys.add(key)

print("After cleaning:", len(cleaned_reviews))

# -----------------------------
# 4️⃣ SAVE FINAL DATASET
# -----------------------------
df = pd.DataFrame({
    "review": cleaned_reviews
})

df.to_csv("nykaa_reviews_clean.csv", index=False)

print("Final dataset saved as nykaa_reviews_clean.csv")
print("Final dataset size:", len(df))
