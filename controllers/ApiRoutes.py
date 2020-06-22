from http import HTTPStatus
from flask import Blueprint, render_template, request, jsonify, Response
import scholarly.scholarly

bp = Blueprint('api', __name__)


@bp.route('/authors/<author_name>', methods=['GET'])
def get_author(author_name):
    try:
        print("author_name : ",author_name)
        # Search by author name and return a generator of Author objects
        search_query = scholarly.search_author(author_name)
        # Populate the Author with information from their profile
        author = next(search_query).fill()

    except Exception as exception:
        print("exception")
        return jsonify(sucess=False,
                       message='author was not found',
                       status=HTTPStatus.NOT_FOUND.value,
                       detatil=HTTPStatus.NOT_FOUND.description,
                       ), HTTPStatus.NOT_FOUND

    try:
        # cache author information for tests
        file_name = author_name.replace(' ', '_').lower() + ".json"
        with open("cache/" + file_name, 'w') as file:
            file.write(author.toJSON())

    except Exception as exception:
        print("exception")
        return jsonify(sucess=False,
                       message=str(exception),
                       status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
                       detatil=HTTPStatus.INTERNAL_SERVER_ERROR.description,
                       ), HTTPStatus.INTERNAL_SERVER_ERROR

    return Response(author.toJSON(), HTTPStatus.OK, mimetype='application/json')
