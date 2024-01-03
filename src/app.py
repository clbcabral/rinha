from flask import Flask, request, jsonify
from flask_uuid import FlaskUUID
from psycopg.errors import DataError, UniqueViolation, NotNullViolation
from db import create_pessoa, get_pessoa, count_pessoa, search_pessoa

app = Flask(__name__)

flask_uuid = FlaskUUID()
flask_uuid.init_app(app)

@app.route('/pessoas', methods=['GET', 'POST'])
def pessoas():
    try:
        if request.method == 'POST' and request.is_json:
            id = create_pessoa(request.get_json())
            return id, 201, {'Location': '/pessoas/%s' % (id)}
        if request.method == 'GET':
            term = request.args.get('t')
            if not term:
                return '', 400
            pessoas = search_pessoa(term)
            return pessoas, 200
    except DataError:
        return '', 400
    except (UniqueViolation, NotNullViolation):
        return '', 422
    except Exception as e:
        app.logger.error(e)
        return '', 500

@app.route('/pessoas/<uuid:id>', methods=['GET'])
def pessoa(id):
    pessoa = get_pessoa(id)
    if pessoa:
        return pessoa, 200
    return '', 404

@app.route('/contagem-pessoas', methods=['GET'])
def total():
    return '%s' % (count_pessoa()), 200