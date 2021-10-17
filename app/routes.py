from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)
#arg1: string used to identify this Blueprint from the Flask server logs
#arg2: uses __name__ to figure where the home folder is

#create an endpoint
@hello_world_bp.route('/hello-world', methods=["GET"])
def get_hello_world():
    my_response_body = "Hello, World!"
    return my_response_body

@hello_world_bp.route('/hello-world/JSON', methods = ['GET'])
def hello_world_json():
    return {
        "name": "Kyra",
        "message" : "Heya",
        "hobbies" : ["coding", "writing", "reading"]
    }, 200
    