from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    #register blueprint -- necessary everytime new blueprint is instantiated
    #registering = tell the app to use endpoints from hello_world_bp for its routing
    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)


    return app
