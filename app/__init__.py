from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return {
        'hello'
    }


@app.route('/api/v1/accounts', methods=['GET'])
@app.route('/api/v1/accounts/', methods=['GET'])
def show_accounts():
    return {
        'William Shakespeare',
        'Linus',
    }


@app.route('/api/v1/quotes', methods=['GET'])
@app.route('/api/v1/quotes/', methods=['GET'])
def show_quotes():
    return {
        'William Shakespeare': {
            'quote': [
                'Love all,trust a few,do wrong to none',
                'Some are born great, some achieve greatness, and some greatness thrust upon them.'
            ]
        },
        'Linus': {
            'quote': [
                'Talk is cheap. Show me the code.'
            ]
        },
    }


@app.route('api/v1/routes', methods=['GET'])
@app.route('api/v1/routes/', methods=['GET'])
def show_routes():
    """List of routes for this API."""
    output = {
        'info': 'GET /api/v1/routes',
        'quotes': 'GET /api/v1/quotes',
        'accounts': 'GET /api/v1/accounts',
    }
    return jsonify(output)
