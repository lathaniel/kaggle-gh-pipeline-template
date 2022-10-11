# virtual environment (python 3.9)
python -m venv .venv && . .venv/Scripts/activate

# Install python packages
python -m pip install -r requirements.txt

# Add the virtualenv as a jupyter kernel (for VS Code)
# note - at this point you may need/want to
# restart VS Code :( to properly activate the kernel
ipython kernel install --name "kaggle-cms" --user

# Create a local directory for kaggle data
mkdir -p kaggle-data && kaggle datasets init -p kaggle-data