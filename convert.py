import json

# Đọc file JSON
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Chuyển đổi các content thành một dòng duy nhất, thay thế \n bằng khoảng trắng
for entry in data:
    content = entry['_source']['content']
    content = content.replace('\n', ' ')  # Loại bỏ các ký tự xuống dòng
    entry['_source']['content'] = content

# In dữ liệu sau khi đã xử lý
for entry in data:
    print("__label__" + str(entry["_source"]["label"]) + " " + entry["_source"]["content"])

# Lưu vào file txt để huấn luyện với FastText
with open("fasttext_data.txt", "w", encoding="utf-8") as f:
    
    for entry in data:
         f.write("__label__" + str(entry["_source"]["label"]) + " " + entry["_source"]["content"] +"\n")

print("Đã lưu dữ liệu vào file 'fasttext_data.txt'")