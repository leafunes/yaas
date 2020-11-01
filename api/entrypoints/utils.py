from json import dumps
from flask import Response
import datetime

def json_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def json(res):
    if res != None:
        if type(res) is list:
            return Response(response = dumps([o.__dict__ for o in res], default=json_converter), content_type = "application/json")
        elif type(res) is dict:
            return Response(response = dumps(res, default=json_converter), content_type = "application/json")
        else:
            return Response(response = dumps(res.__dict__, default=json_converter), content_type = "application/json")
    else:
        return None


def not_found(response):
    return Response(response=response, status=404, content_type = "application/text")

def bad_request(response):
    return Response(response=response, status=400, content_type = "application/text")