from utils import parametrize_over_notebooks
import re
import os


@parametrize_over_notebooks
def test_links(path, filename):
    with open(os.path.join(path, filename)) as f:
        content = f.read()
    for match in re.findall(r"\(([^\)\(]+\.ipynb)\)", content):
        assert os.path.isfile(os.path.join(path, match)), f"Can't find {match}"
