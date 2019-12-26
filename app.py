from flask import Flask, request

import base_62_mapper.base_62_mapper as mapper
import db
import string
from flask.json import jsonify

app = Flask(__name__)
POSSIBLE_CHARS = '0123456789' + string.ascii_lowercase + string.ascii_uppercase
DICT = mapper.Mapper.generate_dict(POSSIBLE_CHARS)
MAPPER = mapper.Mapper
BASE = 'nathanauimpl.ca/'

@app.route('/v1/shorten', methods=['POST'])
def shorten():
    json = request.json
    lengthy_url = json['url']

    # Make the query to see if the row exists in db
    rows = db.get_row(url=lengthy_url)
    row_info = None if len(rows) == 0 else rows[0]

    # if the row already exists in db, then we can finish
    if row_info is None:
        db.insert_row(lengthy_url)
        row_info = db.get_row(url=lengthy_url)
    
    # This is the number of the row containing our record
    # It should then be converted into base 62 (6-digit shortened code)
    row_number = row_info[0]

    # Convert into base 62 (this is the 6-digit code)
    shortened_url_code = MAPPER.to_base_62(row_number, possible_characters=POSSIBLE_CHARS)

    shortened_url = BASE + shortened_url_code

    return jsonify({
        'Given': lengthy_url,
        'Computed': shortened_url
    })
    
@app.route('/v1/lengthen', methods=['POST'])
def lengthen():
    json = request.json
    url = str(json['url'])
    shortened_url = url
    if shortened_url.startswith(BASE):
        shortened_url = shortened_url[len(BASE)::]

    # Get the row number from base62 representation
    row_number = MAPPER.from_base_62_encoded(shortened_url, DICT)

    # Make the query to see if the row exists in db
    rows = db.get_row(id=row_number)
    row_info = None if len(rows) == 0 else rows[0]

    # if the row already exists in db, then we can finish
    if row_info is None:
        return jsonify({
            'Message': 'No lengthy URL exists for this given shortened URL'
        })
    
    lengthy_url = row_info[1]

    return jsonify({
        'Given': url,
        'Computed': lengthy_url
    })
    
if __name__ == '__main__':
    app.run()