from http import HTTPStatus
from flask import Blueprint, jsonify, Response
from os import path

bp = Blueprint('fake-api', __name__)


@bp.route('/authors/<author_name>', methods=['GET'])
def get_test_author(author_name):

    file_name_1 = author_name.replace(' ', '_').lower() + ".json"
    file_name_2 = '_'.join(author_name.split(' ')[::-1]).lower() + ".json"

    author_file_path = str()
    if path.exists('cache/' + file_name_1):
        author_file_path = 'cache/' + file_name_1
    elif path.exists('cache/' + file_name_2):
        author_file_path = 'cache/' + file_name_2

    if author_file_path != "":
        with open(author_file_path, 'r') as author_file:
            author = author_file.read()
        return Response(author, HTTPStatus.OK, mimetype='application/json')

    else:
        return jsonify(sucess=False,
                       message='author was not found',
                       status=HTTPStatus.NOT_FOUND.value,
                       detatil=HTTPStatus.NOT_FOUND.description,
                       ), HTTPStatus.NOT_FOUND
