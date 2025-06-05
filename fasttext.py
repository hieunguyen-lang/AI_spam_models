import fasttext
# Huấn luyện mô hình (giả sử dữ liệu đã được chuẩn bị và lưu vào output.txt)
model = fasttext.train_supervised(input="output.txt", lr=0.1, epoch=25, wordNgrams=2)

# Lưu mô hình vào file
model.save_model("model_fasttext.bin")

# Kiểm tra mô hình đã lưu
print("Mô hình đã được lưu!")