import os
from pathlib import Path

# Final folder structure definition
PROJECT_STRUCTURE = [
    "configs",
    "data/bank/processed",
    "data/bank/raw",
    "data/healthcare/processed",
    "data/healthcare/raw",
    "data/sensors/processed",
    "data/sensors/raw",
    "models",
    "notebooks/tabular",
    "notebooks/images",
    "notebooks/time_series",
    "reports",
    "scripts",
    "src/synthgen/common",
    "src/synthgen/tabular",
    "src/synthgen/images",
    "src/synthgen/time_series",
    "tests"
]

# Default files to create
DEFAULT_FILES = {
    "LICENSE": "",
    "README.md": "# Synthetic Data Generation Project\n",
    "requirements.txt": "# Add your dependencies here\n",
    "reports/README.md": "# Reports and Analysis\n",
    "configs/base.yaml": "# Base config\n",
    "configs/dataset.yaml": "# Dataset configuration\n",
    "configs/model.yaml": "# Model parameters\n",
    "configs/privacy.yaml": "# Privacy settings\n",
    "scripts/init_project.py": "# Future setup script\n",
    "notebooks/exploration.ipynb": "",
    "src/synthgen/__init__.py": "",
    "src/synthgen/app.py": "# Web/Streamlit/FastAPI entry\n",
    "src/synthgen/cli.py": "# CLI entry\n",
    "src/synthgen/common/__init__.py": "",
    "src/synthgen/common/utils.py": "# Shared utilities\n",
    "src/synthgen/common/ingest.py": "# Data ingestion functions\n",
    "src/synthgen/tabular/__init__.py": "",
    "src/synthgen/tabular/preprocess.py": "# Preprocessing for tabular data\n",
    "src/synthgen/tabular/train.py": "# Training for tabular data\n",
    "src/synthgen/tabular/generate.py": "# Generation for tabular data\n",
    "src/synthgen/tabular/evaluate.py": "# Evaluation for tabular data\n",
    "src/synthgen/images/__init__.py": "",
    "src/synthgen/images/preprocess.py": "# Preprocessing for images\n",
    "src/synthgen/images/train.py": "# Training for images\n",
    "src/synthgen/images/generate.py": "# Generation for images\n",
    "src/synthgen/images/evaluate.py": "# Evaluation for images\n",
    "src/synthgen/time_series/__init__.py": "",
    "src/synthgen/time_series/preprocess.py": "# Preprocessing for time-series\n",
    "src/synthgen/time_series/train.py": "# Training for time-series\n",
    "src/synthgen/time_series/generate.py": "# Generation for time-series\n",
    "src/synthgen/time_series/evaluate.py": "# Evaluation for time-series\n",
    "tests/test_basic.py": "# Basic tests\n"
}

def create_structure():
    """Create project folder structure."""
    for folder in PROJECT_STRUCTURE:
        Path(folder).mkdir(parents=True, exist_ok=True)
        print(f"[DIR]  Created: {folder}")

    for file, content in DEFAULT_FILES.items():
        file_path = Path(file)
        if not file_path.exists():
            file_path.write_text(content)
            print(f"[FILE] Created: {file}")
        else:
            print(f"[SKIP] Exists: {file}")

if __name__ == "__main__":
    print("🚀 Setting up Synthetic Data Generation project structure...")
    create_structure()
    print("✅ Setup complete!")
