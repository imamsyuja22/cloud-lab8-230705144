from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # Silahkan ganti <NIM Anda> dengan NIM asli Anda
    return {'pesan': 'Hello from CI/CD', 'nim': '230705144'}

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
