from flask import Flask
from werkzeug import exceptions as Err

app = Flask(__name__)


@app.errorhandler(Err.NotFound)
def handle_bad_request(e):
    return 'Page not found!', 404

# or, without the decorator
# app.register_error_handler(400, handle_bad_request);


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(port=5000)
