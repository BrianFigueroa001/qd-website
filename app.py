import os
from flask import Flask, render_template
from __future__ import print_function

app = Flask(__name__)


@app.route('/')
def open_website():
    ART_DIR = os.getcwd() + "/qd-art"

    if not os.path.isdir(ART_DIR):
        print("Art directory not found.")
        print("Creating directory.")
        os.mkdir(ART_DIR)

    print("Moving to art directory.")
    os.chdir(ART_DIR)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
