from flask import Flask, make_response
from errors.errors import NegativeTotalError, TransactionNotFoundError

from entrypoints.account_entrypoint import blueprint as account_blueprint
from entrypoints.utils import bad_request, not_found

app = Flask("api")

app.register_blueprint(account_blueprint)

@app.errorhandler(NegativeTotalError)
def handle_negative_total_error(e):
    return bad_request(str(e))

@app.errorhandler(TransactionNotFoundError)
def handle_transaction_not_found(e):
    return not_found(str(e))

@app.route('/ping')
def hello():
    return 'pong'