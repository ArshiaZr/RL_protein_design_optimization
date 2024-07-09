import numpy as np

def modify_sequence(sequence, action):
    index = np.random.randint(0, len(sequence))
    new_amino_acid = chr(action + 65)  # Convert action to corresponding amino acid
    modified_sequence = sequence[:index] + new_amino_acid + sequence[index+1:]
    return modified_sequence

def optimize_sequence_with_rl(sequence):
    from env.protein_design_env import ProteinDesignEnv
    import stable_baselines3 as sb3

    env = ProteinDesignEnv(sequence)
    model = sb3.PPO.load("data/trained_model.zip")

    # Assume you have a fixed number of steps or actions to optimize the sequence
    for _ in range(10):  # Example: 10 optimization steps
        obs = env.reset()
        action, _ = model.predict(obs)
        sequence = modify_sequence(sequence, action)

    return sequence
