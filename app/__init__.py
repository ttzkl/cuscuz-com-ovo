from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/api/v1', methods=['GET'])
@app.route('/api/v1/', methods=['GET'])
def index():
    return {
        'hello': 'world',
    }


@app.route('/api/v1/accounts', methods=['GET'])
@app.route('/api/v1/accounts/', methods=['GET'])
def show_accounts():
    return {
        'William Shakespeare': {
            'occupation': [
                'Playwright',
                'Poet',
                'Actor',
            ]
        },
        'Linus Torvalds': {
            'occupation': [
                'Software engineer',
            ]
        },
    }


@app.route('/api/v1/quotes', methods=['GET'])
@app.route('/api/v1/quotes/', methods=['GET'])
def show_quotes():
    return {
        'William Shakespeare': {
            'quote': [
                'Love all,trust a few,do wrong to none',
                'Some are born great, some achieve greatness, and some greatness thrust upon them.',
            ]
        },
        'Linus Torvalds': {
            'quote': [
                'Talk is cheap. Show me the code.',
            ]
        },
    }


@app.route('/api/v1/routes', methods=['GET'])
@app.route('/api/v1/routes/', methods=['GET'])
def show_routes():
    """List of routes for this API."""
    output = {
        'info': 'GET /api/v1/routes',
        'quotes': 'GET /api/v1/quotes',
        'accounts': 'GET /api/v1/accounts',
    }
    return jsonify(output)


@app.errorhandler(404)
def page_not_found(e):
    return {
        'error': e,
    }, 404



@app.errorhandler(500)
def internal_server_error(e):
    return {
        'error': e,
    }, 500
