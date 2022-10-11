# virtual environment (python 3.9)
python -m venv .venv && . .venv/Scripts/activate

# Install python packages
python -m pip install -r requirements.txt

# Convert script to jupyer notebook
jupytext --to ipynb notebook.py