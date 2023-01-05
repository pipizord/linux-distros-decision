from flask import Flask
from flask import render_template
import csv

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello_world(name=None):
    return render_template('index.html', name=name, item_list=get_data_from_external_source())


def get_data_from_external_source():
    result_list = []
    with open('src/external_source.csv', newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            result_list.append(row)
    return result_list