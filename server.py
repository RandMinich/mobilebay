from flask import Flask, render_template, redirect, request, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/check', methods=['POST', 'GET'])
def check():
    name = request.args.get('name')
    password = request.args.get('password')

@app.route('/docs', methods=['POST'])
def documents():
    json_file = None
    return json_file

def main():
    app.run()

if __name__ == '__main__':
    while True:
        main()