from flask import Flask

app = Flask(__name__)


@app.route('/message')
def get_message():
    return {
        'message': 'test'
    }


if __name__ == '__main__':
    app.run()
