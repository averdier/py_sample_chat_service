# -*- coding: utf-8 -*-

import os
from app import create_app

app = create_app('default')


if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT, debug=True)  # On Windows
    # app.run(HOST, PORT, debug=True, processes=3) # On Linux