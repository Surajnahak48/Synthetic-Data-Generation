import os

# Define the folder structure
folders = [
    "configs",
    "data/raw",
    "data/processed",
    "data/synthetic",
    "notebooks",
    "reports",
    "src/synthgen",
    "tests"
]

# Files to create with initial content
files_with_content = {
    "configs/dataset.yaml": "# Dataset configuration\n",
    "configs/model.yaml": "# Model configuration\n",
    "configs/privacy.yaml": "# Privacy settings configuration\n",
    "notebooks/exploration.ipynb": "",
    "reports/README.md": "# Reports and analysis go here\n",
    "src/synthgen/__init__.py": "",
    "src/synthgen/ingest.py": "# Code to load and scan data\n",
    "src/synthgen/preprocess.py": "# Data preprocessing code\n",
    "src/synthgen/train.py": "# Train synthetic data generator models\n",
    "src/synthgen/generate.py": "# Generate synthetic data samples\n",
    "src/synthgen/evaluate.py": "# Evaluate fidelity, utility, and privacy\n",
    "src/synthgen/cli.py": "# Command-line interface for the project\n",
    "src/synthgen/app.py": "# Streamlit or FastAPI app for the project\n",
    "tests/test_basic.py": "def test_placeholder():\n    assert True\n",
    "requirements.txt": "# List of dependencies\npandas\nnumpy\nscikit-learn\nsdv\nsdmetrics\n",
    "README.md": "# Synthetic Data Generation Project\n\nThis project generates privacy-preserving synthetic datasets.\n"
}

def create_structure():
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")
    
    # Create files with initial content
    for file_path, content in files_with_content.items():
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_structure()
    print("\n Project structure created successfully!")
