def predict_stability(protein_sequence):
    # Dummy implementation for example
    return len(protein_sequence) / 100

def predict_binding_affinity(protein_sequence, target_ligand=None):
    # Dummy implementation for example
    return len([aa for aa in protein_sequence if aa in 'ACDEFGHIKLMNPQRSTVWY']) / 20

def predict_catalytic_activity(protein_sequence):
    # Dummy implementation for example
    return len([aa for aa in protein_sequence if aa in 'DEHK']) / 10

def fitness_function(protein_sequence):
    stability_score = predict_stability(protein_sequence)
    binding_affinity_score = predict_binding_affinity(protein_sequence)
    catalytic_activity_score = predict_catalytic_activity(protein_sequence)
    fitness = (stability_score + binding_affinity_score + catalytic_activity_score) / 3
    return fitness
