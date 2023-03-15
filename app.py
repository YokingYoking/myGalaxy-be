from flask import Flask, request
from bioblend import galaxy
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')
gi = galaxy.GalaxyInstance(url='https://usegalaxy.org/', key='5708d9d457c6681669c3ad03027263ba')
hi = gi.histories
di = gi.datasets
ti = gi.tools


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getHistory')
def get_history():
    return hi.get_histories()


@app.route('/getDataset')
def get_dataset():
    return di.get_datasets(100, 0)


@app.route('/downloadDataset')
def download_dataset():
    did = request.args.get("id", type=str)
    return di.download_dataset(dataset_id=did)


@app.route('/showHistory')
def show_history():
    hid = request.args.get("id", type=str)
    hi.show_history(history_id=hid)


@app.route('/getTools')
def get_tools():
    return ti.get_tools()


# examples
@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    return "Blog Id is: %s" % blog_id


if __name__ == '__main__':
    app.run(debug=True)
