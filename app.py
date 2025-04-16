from flask import Flask
from routes.auth import auth_bp
from routes.feeds import feeds_bp
from database.db import*

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(feeds_bp, url_prefix="/feeds")

if __name__ == '__main__':
    app.run(debug=True)
