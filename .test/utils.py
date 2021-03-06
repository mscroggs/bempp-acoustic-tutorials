import pytest
import os

root_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")

notebooks = [(root_path, "README.ipynb")]
for dir in ["exercises", "tutorials"]:
    path = os.path.join(root_path, dir)
    for i in os.listdir(path):
        if i.endswith(".ipynb"):
            notebooks.append((path, i))


parametrize_over_notebooks = pytest.mark.parametrize(
    "path, filename", notebooks)
