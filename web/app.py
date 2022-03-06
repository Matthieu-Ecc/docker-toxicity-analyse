from flask import Flask

from routes import configure_routes

from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

configure_routes(app)

metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")
