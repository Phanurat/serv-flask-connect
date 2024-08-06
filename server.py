from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_script():
    data = request.get_json()
    script_name = data.get('script_name')
    
    try:
        result = subprocess.run(['python', script_name], capture_output=True, text=True, check=True)
        return jsonify({
            'success': True,
            'output': result.stdout
        })
    except subprocess.CalledProcessError as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'output': e.output
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
