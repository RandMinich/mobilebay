from flask import Flask, render_template, redirect, request, abort
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/check', methods=['POST', 'GET'])
def check():
    name = request.args.get('name')
    password = request.args.get('password')
    return True

@app.route('/docs', methods=['POST'])
def documents():
    json_file = {}
    return json.dumps(json_file)


@app.route('/notif', methods=['POST', 'GET'])
def notifications():
    name = request.args.get('name')
    password = request.args.get('password')

def main():
    app.run()

if __name__ == '__main__':
    while True:
        main()