from flask import Flask, render_template, request, redirect, Response, current_app, session
from database import get_download_history
import controller
from database import connect_to_database, save_download_history, get_download_history
import json
app = Flask(__name__)

db_connection = connect_to_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/terms-conditions')
def terms():
    return render_template('terms-conditions.html')

@app.route('/history')
def history():
    history_data = get_download_history(db_connection)
    return render_template('history.html', videos=history_data)

@app.route('/download', methods=[ "GET"])
def download():
    output = []
    url = request.args["url"]
    print(url)
    type = request.args["type"]
    data = {'url': url, 'type': type}
    output.append(data)
    return controller.downloadProcess(output)

@app.route('/claimlink/', methods=[ "GET"])
def claimlink():
    url = request.args["url"]
    print(url)
    return controller.claimLink(url)

def run():
    app.run(port=8000, debug=True)

