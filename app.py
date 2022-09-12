import flask
from flask import request
from base import *
import datetime



app = flask.Flask('app')
create_table()

class HttpError(Exception):
    def __init__(self, status_code: int, message):
        self.status_code = status_code
        self.message = message

@app.errorhandler(HttpError)
def handle_invalid_usage(error):
    response = flask.jsonify({"message": error.message})
    response.status_code = error.status_code
    return response





@app.route('/get/', methods=['GET'])
def get():
    qs = request.args
    ds = int(qs['param'])
    if ds > 0:
        scan_table(qs['param'])
        return flask.jsonify({
            'id': answer['id'],
            'heading': answer['heading'],
            'description': answer['description'],
            'date_of_creation': answer['date_of_creation'],
            'user_name': answer['user_name'],
        })
    else:
        raise HttpError(400, 'Запрос неотправлен,неправильно указан id обьявления')


@app.route('/post/', methods=['POST'])
def post():
    json_date = request.json
    date_of_creation = datetime.datetime.now()
    if 'id' in json_date:
        zapolnenie_table(json_date['id'], json_date['heading'], json_date['description'], date_of_creation, json_date['user_name'])
        return flask.jsonify({
            'message': 'POST Запрос отправлен'
        })
    else:
        raise HttpError(400, 'Неправильно указан  один из ключевых параметров ( пример:id,heading и т.д.)')


@app.route('/delete/', methods=['DELETE'])
def delete():
    qs = request.args
    ds = int(qs['param'])
    if ds > 0:
        delete_announcement(qs['param'])
        return flask.jsonify({
            'message': f'Обьявление с id_{ds} удалено'
        })
    else:
        raise HttpError(400, f'Запрос неоправлен,неправильно указан id_{ds}  обьявления на удаление')


app.run(threaded=True)


























