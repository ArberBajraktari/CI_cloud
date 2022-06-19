from flask import Flask
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():
    resp = requests.get('http://0.0.0.0:80/getData')
    return 'Response from TestRequest: '+resp.text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# testing
# sad
