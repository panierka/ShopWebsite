from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/message')
def get_message():
    return {
        'message': 'test'
    }


if __name__ == '__main__':
    app.run()
