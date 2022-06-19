from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)
count = 0

@app.route('/')
def index():
    output = "No request is made"
    return render_template('home.html',output=output)


@app.route('/<output>')
def data_requested(output):
    return render_template('home.html',output=output)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    global count
    if count%2 == 0:
        output = "bravo"
    else:
        output = "asht tu punu"
    count+=1
    #resp = requests.get('http://0.0.0.0:80/getData')
    return redirect(url_for('data_requested', output=output))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


#resp = requests.get('http://0.0.0.0:80/getData')
#return 'Response from TestRequest: '+resp.text