from flask import Flask

CERT_FILE = 'certs/localhost.pem'
KEY_FILE = 'certs/localhost-key.pem'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Server is running away from you."

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello from KP-21 Khandokhin Oleksandr'

if __name__=='__main__':
    context=(CERT_FILE, KEY_FILE)
    app.run(host='0.0.0.0', port=2125, debug=True, ssl_context=context)