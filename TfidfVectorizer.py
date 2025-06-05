from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import json
# Đọc file JSON
with open("converted_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data)
# Chia dữ liệu thành X (văn bản) và y (nhãn)
X = df['text']
y = df['label']

# Chia dữ liệu thành train và test (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Tạo đối tượng TfidfVectorizer
vectorizer = TfidfVectorizer()

# Chuyển đổi văn bản thành vectơ
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Tạo đối tượng Logistic Regression
model = LogisticRegression()

# Huấn luyện mô hình
model.fit(X_train_tfidf, y_train)

# Lưu mô hình Logistic Regression
joblib.dump(model, 'logistic_regression_model.pkl')

# Lưu TfidfVectorizer
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

print("Mô hình và vectorizer đã được lưu thành công.")
