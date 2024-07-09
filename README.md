# Intelligent Protein Design Optimization using Reinforcement Learning (RL)

## Project Overview

This project utilizes reinforcement learning (RL) to optimize protein sequences, aiming to enhance properties such as stability, binding affinity, or catalytic activity. Researchers can adjust parameters and refine the reward system to tailor optimizations based on specific protein design objectives.

## File Structure

- **api/**: Contains files for the API service.
- **env/**: Includes the environment setup for the RL agent.
- **models/**: Contains files related to model training and storage.
- **ui/**: Contains files for the user interface.
- **utils/**: Provides utility functions.
- **data/**: Holds data files.
- **notebooks/**: Contains Jupyter notebooks for exploration and experimentation.

## Setup Instructions

1. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:

   ```bash
   python -m models.train_model
   ```

4. Run the API service:

   ```bash
   python -m api.app
   ```

5. Launch the Streamlit UI:
   ```bash
   streamlit run ui/app.py
   ```

## Usage

- Streamlit UI will be available in your localhost
- Input a protein sequence in the UI and click "Optimize" to observe the optimized sequence.

## Customization

Researchers can modify the following aspects to optimize proteins:

- **Environment Setup**: Adjust the environment parameters in `env/protein_design_env.py`.
- **Model Training**: Fine-tune training settings and hyperparameters in `models/train_model.py`.
- **Reward System**: Tailor the reward function in `env/protein_design_env.py` to prioritize specific protein properties.

## Author

- Arshia Zakeri Rad
