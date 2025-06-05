import websocket

def on_message(ws, message):
    print(f"Kiểu dữ liệu của message: {type(message)}")
    if isinstance(message, str):
        print(f"Nhận được văn bản: {message}")
    else:
        print("Đây là dữ liệu không phải văn bản (có thể là nhị phân).")

# Hàm xử lý lỗi
def on_error(ws, error):
    print(f"Lỗi xảy ra: {error}")

# Hàm khi kết nối đóng
def on_close(ws, close_status_code, close_msg):
    print("WebSocket đã đóng kết nối.")

# Hàm khi kết nối mở
def on_open(ws):
    print("Đã kết nối tới WebSocket.")
    # Bạn có thể gửi tin nhắn hoặc dữ liệu sau khi kết nối mở
    ws.send("Hello, WebSocket!")  # Gửi thông điệp đến WebSocket nếu cần

# Kết nối tới WebSocket
ws = websocket.WebSocketApp("wss://edge-chat.facebook.com/chat?region=hil&sid=7899851865980927&cid=32d319c8-ed01-4bfd-9944-57fc2018b7f5clear",  # Thay thế bằng URL WebSocket của bạn
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close,
                            on_open=on_open)

# Bắt đầu nhận dữ liệu từ WebSocket
ws.run_forever()
