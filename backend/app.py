from flask import Flask, url_for
from flask_restplus import Api
from werkzeug.middleware.proxy_fix import ProxyFix
from config import config
from os import getenv

from resources.allocation import api as ns_allocation
from resources.fund import api as ns_fund

APP_ENV = getenv('APP_ENV', 'dev')
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object(config[APP_ENV])

api = Api(app, version='1.0', title='Investment Advisor Api', prefix='/api')

api.add_namespace(ns_allocation)
api.add_namespace(ns_fund)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
