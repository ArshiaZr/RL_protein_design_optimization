from flask import Flask, jsonify
from api.optimization_service import optimize_protein

app = Flask(__name__)

@app.route('/optimize', methods=['POST'])
def optimize_protein_endpoint():
    return optimize_protein()

if __name__ == '__main__':
    app.run()