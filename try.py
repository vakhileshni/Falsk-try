from flask import Flask, request, jsonify, render_template
application = Flask(__name__)
@application.route('/')
def home():
    return "Hello world"

if __name__ == "__main__":
    application.run(host='0.0.0.0',port=80)
