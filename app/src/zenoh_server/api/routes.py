import time
import zenoh
import asyncio
import threading
import random
from libs import validate_code_block
from flask import Blueprint, request, jsonify

# Create a Blueprint for the subscription routes
subscribe_bp = Blueprint("subscribe", __name__)


@subscribe_bp.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.get_json()
    key_expr = data.get("key_expr")
    user_expr = data.get("user_expr")


    try:
        # b = compile("def user_defined_function(msg):\n\treturn msg", 'cb', 'exec')
        exec(code_str)
        return jsonify({"key" : key_expr, "cb" : user_defined_function('hello')}) # type: ignore
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    
code_str = """
def user_defined_function(msg):
    return msg
"""