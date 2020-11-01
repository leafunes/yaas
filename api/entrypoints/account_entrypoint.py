
from entrypoints.utils import json, bad_request, not_found
from services.AccountService import AccountService

from flask import Blueprint, request

blueprint = Blueprint('account', __name__)

service = AccountService()


@blueprint.route("/account", methods=['GET'])
def account():
    if request.method == "GET":
        return {"summary": service.get_account_summary()}
    else:
        return not_found()

@blueprint.route("/transactions", methods=['GET'])
def transactions():
    if request.method == "GET":
        return json(service.get_transactions())
    else:
        return not_found()


@blueprint.route("/transactions/credit", methods=['POST'])
def post_credit():
    if request.method == "POST":
        body = request.get_json()
        
        amount = body["amount"]
        description = body["description"]

        if amount <= 0:
            return bad_request("Negative amount not allowed. If you want to debit money please POST to /transactions/debit")

        tr = service.create_credit(amount, description)

        return json(tr)
    else:
        return not_found()
        
@blueprint.route("/transactions/debit", methods=['POST'])
def post_debit():
    if request.method == "POST":
        body = request.get_json()
        
        amount = body["amount"]
        description = body["description"]

        if amount <= 0:
            return bad_request("Negative amount not allowed.")

        tr = service.create_debit(amount, description)

        return json(tr)
    else:
        return not_found()

@blueprint.route("/transactions/<id>", methods=['GET'])
def transactions_by_id(id):
    if request.method == "GET":
        if id is None or not id.isnumeric():
            return bad_request("Id must be a number")
        return json(service.get_transaction_by_id(int(id)))
    else:
        return not_found()