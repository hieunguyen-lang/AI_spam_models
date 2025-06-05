import joblib

# Load mô hình đã lưu
model = joblib.load('logistic_regression_model.pkl')

# Load vectorizer đã lưu
vectorizer = joblib.load('tfidf_vectorizer.pkl')
def classify(text):
    # Vector hóa văn bản
    vector = vectorizer.transform([text])
    
    # Dự đoán nhãn
    prediction = model.predict(vector)[0]

    return prediction


sample_text = "Mình cần tìm thiết kế website cho Spa"
label = classify(sample_text)

print(f"Nội dung: {sample_text}")
print(f"→ Dự đoán nhãn: {label}")
