import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from src.bertcli.menus._menu import Menu

class DimensionalityReductionMenu(Menu):
    def __init__(self):
        is_root = False
        is_leaf = True
        options = [
            "UMAP",
            "PCA",
            "t-SNE",
            "Truncated SVD",
            "Factor Analysis",
        ]

        super().__init__(options, is_leaf, is_root)