import os
from flask import Flask, jsonify, make_response
app = Flask(__name__)

@app.route('/status', methods=['GET'])
def get_status():
    info = {?!?jedi=0, ?!?                      (*_*key: str*_*, default: _T) ?!?jedi?!?
        'version': os.getenv('VER?!?jedi=1, SION'),?!? (*_*key: str*_*) ?!?jedi?!?'
        'lastcommitsha': os.getenv('LAST_COMMIT_SHA'),
        'description': 'pre-interview technical test'
    }

    return jsonify({'myapplication': info})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True)
