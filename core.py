import json
import pandas as pd
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import Trainer, TrainingArguments
# Tải mô hình BERT và tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)



# Đọc JSON từ file
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Lấy content và label từ mỗi _source
records = [{"content": item["_source"]["content"], "label": item["_source"]["label"]} for item in data]

# Tạo DataFrame
df = pd.DataFrame(records)

# Xem thử
print(df.head())

# Nếu label là chuỗi rỗng thì xử lý thành NaN hoặc 0, 1 tùy ý
df['label'] = pd.to_numeric(df['label'], errors='coerce')  # label "" thành NaN
df = df.dropna(subset=['label'])  # loại bỏ dòng thiếu label

# Lấy ra list để huấn luyện
texts = df['content'].tolist()
labels = df['label'].astype(int).tolist()


# Mã hóa văn bản thành input cho BERT
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

# Tạo bộ dữ liệu tùy chỉnh
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, texts, labels, tokenizer):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoding = self.tokenizer(text, padding='max_length', truncation=True, max_length=512)  # KHÔNG return_tensors
        encoding['labels'] = label
        return encoding

# Tạo dataset
dataset = CustomDataset(texts, labels, tokenizer)

# Huấn luyện mô hình
# training_args = TrainingArguments(
#     output_dir='./results',          
#     num_train_epochs=3,              
#     per_device_train_batch_size=8,  
#     per_device_eval_batch_size=16,  
#     warmup_steps=500,               
#     weight_decay=0.01,               
#     logging_dir='./logs',           
#     logging_steps=10,
#     no_cuda=True  # Tắt GPU nếu không sử dụng
# )
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=4,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    learning_rate=2e-5,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    evaluation_strategy="epoch",
    save_strategy="no",  # Không lưu giữa chừng
)
trainer = Trainer(
    model=model,                         
    args=training_args,                  
    train_dataset=dataset,         
)

trainer.train()
