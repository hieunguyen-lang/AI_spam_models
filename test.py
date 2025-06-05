import json

def convert_and_save_json(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    converted = []
    for item in raw_data:
        content = item.get('_source', {}).get('content', '').strip()
        label = item.get('_source', {}).get('label', None)
        if content and label != "":
            converted.append({
                'text': content.replace('\n', ' ').replace('\r', '').strip(),
                'label': int(label)
            })

    # Ghi ra file JSON mới
    with open(output_path, 'w', encoding='utf-8') as out_f:
        json.dump(converted, out_f, ensure_ascii=False, indent=4)

    print(f"✅ Đã ghi {len(converted)} mẫu vào '{output_path}'")

# Gọi hàm
convert_and_save_json('data.json', 'converted_data.json')
