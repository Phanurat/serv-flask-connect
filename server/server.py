from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_script():
    data = request.get_json()
    if not data or 'script_name' not in data:
        return jsonify({'success': False, 'error': 'Invalid request: script_name not provided'}), 400

    script_name = data['script_name']
    script_path = os.path.join(os.path.dirname(__file__), script_name)

    if not os.path.isfile(script_path):
        return jsonify({'success': False, 'error': f'Script {script_name} not found'}), 400

    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
        return jsonify({'success': True, 'output': result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'error': str(e), 'output': e.output}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
