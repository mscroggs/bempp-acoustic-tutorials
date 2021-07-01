import nbformat
import os
from nbconvert.preprocessors import ExecutePreprocessor
from utils import parametrize_over_notebooks


@parametrize_over_notebooks
def test_run_notebook(path, filename):
    with open(os.path.join(path, filename)) as f:
        nb = nbformat.read(f, as_version=4)
    for i, j in enumerate(nb["cells"]):
        if j["cell_type"] == "code":
            nb["cells"][i]["source"] = nb["cells"][i]["source"].replace(
                "plt.show()", "")

    ep = ExecutePreprocessor(timeout=600)
    ep.preprocess(nb, {"metadata": {"path": path}})
