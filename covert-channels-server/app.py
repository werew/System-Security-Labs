from os import listdir
from os.path import isfile, join, dirname, realpath
import random
from flask import Flask, send_from_directory

app = Flask(__name__)

imagedir = dirname(realpath(__file__)) + "/images/"


# This is not really needed
@app.route('/')
def hello_world():
    return 'Random cat image server!'


# Serve a random cat picture!
@app.route('/randomcat')
def randomcat():
    images = [f for f in listdir(imagedir) if isfile(join(imagedir, f))]
    image = random.choice(images)
    return send_from_directory(imagedir, image, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host="0.0.0.0")