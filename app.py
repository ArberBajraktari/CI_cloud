from flask import Flask, render_template, request, redirect, url_for
import time
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
    page = ''
    while page == '':
        try:
            page = requests.get('http://0.0.0.0:80/getData')
            break
        except:
            print("Connection refused by the server..")
            print("ZZzzzz...")
            time.sleep(2)
            print("Was a nice sleep, now let me continue...")
            count += 1
            if count == 3:
                page = """The connection to the API could not be established.
                Please check if the API is running!"""
                break
            continue
    return redirect(url_for('data_requested', output=page))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

