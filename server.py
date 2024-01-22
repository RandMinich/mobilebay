import json

from flask import Flask, request

from data.db_session import create_session
from data.events import Events
from data.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
session = create_session()


@app.route('/check', methods=['POST', 'GET'])
def check():
    name = request.args.get('name')
    password = request.args.get('password')
    if session.query(User).filter(User.login == name).filter(User.password == password).first() != None:
        return '+'
    return '-'


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.args.get('name')
    login = request.args.get('login')
    password = request.args.get('password')
    if name != None and login != None and password != None:
        if session.query(User).filter(User.login == login).filter(User.password == password).first() == None:
            u = User(name=name, login=login, password=password)
            session.add(u)
            session.commit()
            return '+'
        else:
            return 'YourAccountAlreadyExist'


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
    lan = None
    lon = None
    author = None
    text = None
    if request_data:
        if 'lan' in request_data:
            lan = request_data['lan']
        if 'lon' in request_data:
            lon = request_data['lon']
        if 'author' in request_data:
            author = request_data['author']
        if 'text' in request_data:
            text = request_data['text']
        ev = Events(lan=lan, lon=lon, author_id=author, description=text)
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
