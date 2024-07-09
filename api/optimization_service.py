from flask import request, jsonify
from utils.sequence_modification import optimize_sequence_with_rl

def optimize_protein():
    data = request.json
    sequence = data['sequence']
    optimized_sequence = optimize_sequence_with_rl(sequence)
    return jsonify({'optimized_sequence': optimized_sequence})