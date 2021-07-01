import nbformat
import os


def test_readme():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")

    with open(os.path.join(path, "README.md")) as f:
        content = f.readlines()

    for i, line in enumerate(content):
        if "nbviewer" in line:
            content = content[:i] + content[i + 2:]
            break

    with open(os.path.join(path, "README.ipynb")) as f:
        nb = nbformat.read(f, as_version=4)

    assert "".join(content) == nb["cells"][0]["source"]
