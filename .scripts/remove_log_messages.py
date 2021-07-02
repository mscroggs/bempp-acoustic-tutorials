import os
import nbformat
from sys import argv

notebooks = []
for dir in ["../exercises", "../tutorials"]:
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dir)
    for i in os.listdir(path):
        if i.endswith(".ipynb"):
            with open(os.path.join(path, i)) as f:
                content = nbformat.read(f, as_version=4)

            for n, c in enumerate(content["cells"]):
                if c["cell_type"] == "code" and "outputs" in c:
                    content["cells"][n]["outputs"] = [
                        j for j in c["outputs"] if "name" not in j or j["name"] != "stderr"
                    ]
            with open(os.path.join(path, i), "w") as f:
                nbformat.write(content, f)
