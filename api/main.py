import os
import sys

from flask import Flask, jsonify, render_template
from flask_cors import CORS
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.routes.appRoutes import app_routes

import pkg_resources





app = Flask(__name__)
app.debug = True
CORS(app)   
app_routes(app)

def check_packages():
    packages_to_check = ["langchain==0.0.340", "llama_index==0.9.11", "flask==2.3.2", "flask_cors==3.0.10"]
    results = {}

    for package in packages_to_check:
        package_name, _, desired_version = package.partition("==")
        installed_version = None

        try:
            installed_version = pkg_resources.get_distribution(package_name).version
            if installed_version == desired_version:
                results[package] = "installed"
            else:
                results[package] = f"installed, but version {installed_version} instead of {desired_version}"
        except pkg_resources.DistributionNotFound:
            results[package] = "not installed"

    return results
@app.route('/check_packages', methods=['GET'])

def route_check_packages():
    results = check_packages()
    return jsonify(results)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    # # print(os.environ.get('OPENAI_API_KEY'))   
    # results = check_packages()
    # print(results)

    app.run()
