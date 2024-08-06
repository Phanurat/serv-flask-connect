import socket

# สร้าง socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# กำหนด host และ port
host = '192.168.31.248'
port = 12345

# ผูก socket กับ host และ port
server_socket.bind((host, port))

# ฟังการเชื่อมต่อ
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    # ยอมรับการเชื่อมต่อจาก client
    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")

    # ส่งข้อความไปยัง client
    client_socket.send(b"Thank you for connecting")
    
    # ปิดการเชื่อมต่อกับ client
    client_socket.close()
