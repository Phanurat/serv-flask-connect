import requests

url = 'http://192.168.31.95:5000/run'  # แก้ไขไอพีแอดเดรสให้ตรงกับ server
script_name = 'main.py'  # ชื่อไฟล์ Python ที่ต้องการให้ server รัน

data = {'script_name': script_name}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # ตรวจสอบสถานะการตอบกลับ
    result = response.json()
    if result['success']:
        print('Output from script:')
        print(result['output'])
    else:
        print('Error running script:')
        print(result['error'])
except requests.exceptions.RequestException as e:
    print(f'Failed to communicate with server: {e}')
