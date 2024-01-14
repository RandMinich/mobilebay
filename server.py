from flask import Flask, render_template, redirect, request, abort
from data.db_session import create_session
from data.events import Events
from data.coords import Coords
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
session = create_session()
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

@app.route('/geo', methods=['POST'])
def give_coords():
    request_data = request.get_json()

    coords = None
    author = None
    text = None
    if request_data:
        if 'coords' in request_data:
            coords = request_data['coords']
        if 'author' in request_data:
            author = request_data['author']
        if 'text' in request_data:
            text = request_data['text']
        cor = Coords(coord=coords)
        ev = Events(coord=cor.id, author_id=author, description=text)
        session.add(cor)
        session.add(ev)
    return 'good'


@app.route('/get_geo', methods=['POST', 'GET'])
def get_coords():
    ev = list(Events.query.all())
    return ev



def main():
    app.run()

if __name__ == '__main__':
    while True:
        main()