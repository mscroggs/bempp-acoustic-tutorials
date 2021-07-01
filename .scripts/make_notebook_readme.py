import json
import os

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")

with open(os.path.join(path, "README.md")) as f:
    content = f.readlines()

for i, line in enumerate(content):
    if "nbviewer" in line:
        content = content[:i] + content[i + 2:]
        break

with open(os.path.join(path, "README.ipynb"), "w") as f:
    json.dump({
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": content}],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.5"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }, f)
