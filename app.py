from flask import Flask, request
from bioblend import galaxy

app = Flask(__name__)  # __name__代表当前app.py这个模块

gi = galaxy.GalaxyInstance(url='https://usegalaxy.org/', key='5708d9d457c6681669c3ad03027263ba')

hl = gi.histories.get_histories()
hist = gi.histories.list()[0]
inputs = hist.get_datasets()[:2]


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getHistory')
def get_history():
    return hl


@app.route('/getDataset')
def get_dataset():
    return inputs


# example
@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    return "Blog Id is: %s" % blog_id


# example2
# /blog/list?page=1
@app.route('/blog/list')
def blog_list():
    page = request.args.get("page", default=1, type=int)
    return f"You get Page {page}"


if __name__ == '__main__':
    app.run(debug=True)
