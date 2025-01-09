from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello People,This is a new Gitops project.TY!!!'