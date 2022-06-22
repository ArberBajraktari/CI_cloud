from flask import Flask, render_template, request, redirect, url_for
import requests, json

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


def get_data():
    data = None
    try:
        page = requests.get("http://localhost:80/")
        data = page.text
    except Exception as e:
        print(e)
        data = "No data available. Check your backend."
    return data


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html")


@app.route("/get_data")
def data_requested(data):
    return render_template("home.html", data=data)


@app.route("/handle_data", methods=["POST"])
def handle_data():
    data = get_data()
    return render_template("home.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
