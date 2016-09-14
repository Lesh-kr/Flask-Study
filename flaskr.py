import os

from flaskr import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.config.from_pyfile('config.py')
    app.run(host='127.0.0.1', port=port, debug=True)
