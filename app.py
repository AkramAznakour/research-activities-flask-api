from flask import Flask
from flask_cors import CORS
import scholarly.scholarly

app = Flask(__name__)
cors = CORS(app)


@app.route('/authors/<author_name>', methods=['GET'])
def get_author(author_name):
    
    print("stage one :")
    print(author_name)

    search_query = scholarly.search_author(author_name)
    print("stage two :")
    print(search_query)

    author = next(search_query).fill()
    print("stage three :")
    print(author)

    return author.toJSON()

@app.route('/test/authors/<author_name>', methods=['GET'])
def get_test_author(author_name):
    f = open("json.txt", "r")
    return f.read()


if __name__ == '__main__':
    app.run()
