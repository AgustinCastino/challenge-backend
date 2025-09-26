from flask import Flask
from routes.userRoutes import users
from routes.reportRoutes import report
from routes.loginRoutes import login
from config.mongo import mongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)

@app.route("/")
def index():
    return "Challenge Backend Leafnoise"

app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(report, url_prefix='/report')
app.register_blueprint(login, url_prefix='/login')

if __name__ == "__main__":
    app.run(debug=True)


