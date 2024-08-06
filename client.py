import requests

url = 'http://<server-ip>:5000/run'
script_name = 'test_script.py'  # ชื่อไฟล์ Python ที่ต้องการให้ server รัน

data = {
    'script_name': script_name
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    if result['success']:
        print('Output from script:')
        print(result['output'])
    else:
        print('Error running script:')
        print(result['error'])
else:
    print('Failed to communicate with server')
