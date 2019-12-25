from flask import Flask, request

import base_62_mapper.base_62_mapper as mapper
import db
import string
from flask.json import jsonify

app = Flask(__name__)
POSSIBLE_CHARS = '0123456789' + string.ascii_lowercase + string.ascii_uppercase
DICT = mapper.Mapper.generate_dict(POSSIBLE_CHARS)
MAPPER = mapper.Mapper

@app.route('/v1/shorten', methods=['POST'])
def home():
    json = request.json
    lengthy_url = json['url']

    # Make the query to see if the row exists in db
    row = db.get_row('WHERE url = ' + lengthy_url)

    # if the row already exists in db, then we can finish
    if row is None:
        # db.
        pass

    
if __name__ == '__main__':
    app.run()