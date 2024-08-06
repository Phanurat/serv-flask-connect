import socket

# สร้าง socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# กำหนด host และ port ของ server
host = '192.168.31.95'
port = 12345

# เชื่อมต่อไปยัง server
client_socket.connect((host, port))

# รับข้อมูลจาก server
message = client_socket.recv(1024)
print(message.decode('utf-8'))

# ปิดการเชื่อมต่อ
client_socket.close()
