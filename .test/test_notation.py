import nbformat
import os
from nbconvert.preprocessors import ExecutePreprocessor
from utils import parametrize_over_notebooks

notations = [
    ["\\mathsf{V}", "\\mathsf{K}", "\\mathsf{W}", "\\mathsf{K}'", "\\mathcal{V}", "\\mathcal{K}"],
    ["\\mathsf{S}", "\\mathsf{D}", "\\mathsf{H}", "\\mathsf{A}", "\\mathcal{S}", "\\mathcal{D}"]
]

used = None


@parametrize_over_notebooks
def test_notation_in_notebooks(path, filename):
    global used

    with open(os.path.join(path, filename)) as f:
        content = f.read()

    if used is None:
        for i, n in enumerate(notations):
            for j in n:
                if j in content:
                    used = i
                    break
            else:
                continue
            break

    for i, n in enumerate(notations):
        if i != used:
            for j in n:
                assert j not in content
