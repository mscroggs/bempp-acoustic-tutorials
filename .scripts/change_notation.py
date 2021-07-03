import os
from sys import argv

assert len(argv) == 2

assert argv[1] in ["SDAH", "Bempp"]

notebooks = []
for dir in ["../exercises", "../tutorials"]:
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dir)
    for i in os.listdir(path):
        if i.endswith(".ipynb"):
            with open(os.path.join(path, i)) as f:
                content = f.read()

            if argv[1] == "SDAH":
                content = content.replace("\\mathsf{V}", "\\mathsf{S}")
                content = content.replace("\\mathsf{K}'", "\\mathsf{A}")
                content = content.replace("\\mathsf{K}", "\\mathsf{D}")
                content = content.replace("\\mathsf{W}", "\\mathsf{H}")
                content = content.replace("\\mathsf{Id}", "\\mathsf{I}")
                content = content.replace("\\mathcal{V}", "\\mathcal{S}")
                content = content.replace("\\mathcal{K}", "\\mathcal{D}")

            if argv[1] == "Bempp":
                content = content.replace("\\mathsf{S}", "\\mathsf{V}")
                content = content.replace("\\mathsf{D}", "\\mathsf{K}")
                content = content.replace("\\mathsf{A}", "\\mathsf{K}'")
                content = content.replace("\\mathsf{H}", "\\mathsf{W}")
                content = content.replace("\\mathsf{I}", "\\mathsf{Id}")
                content = content.replace("\\mathcal{S}", "\\mathcal{V}")
                content = content.replace("\\mathcal{D}", "\\mathcal{K}")

            with open(os.path.join(path, i), "w") as f:
                f.write(content)
