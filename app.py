
from flask import Flask
from flask_cors import CORS

from controllers import ApiRoutes, ErrorRoutes, FakeApiRoutes

app = Flask(__name__)
cors = CORS(app)

# Blueprint register
app.register_blueprint(ApiRoutes.bp)
app.register_blueprint(FakeApiRoutes.bp,url_prefix='/fake-api')
app.register_blueprint(ErrorRoutes.bp)

if __name__ == '__main__':
    app.run()
