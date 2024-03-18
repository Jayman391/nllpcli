import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from src.bertcli.menus._menu import Menu

class EmbeddingsMenu(Menu):
    def __init__(self):
        is_root = False
        is_leaf = True
        options = [
            "all-MiniLM-L6-v2",
            "all-MiniLM-L12-v2",
            "Muennighoff/SGPT-125M-weightedmean-msmarco-specb-bitfit",
            "Muennighoff/SGPT-125M-weightedmean-nli-bitfit",
            "multi-qa-MiniLM-L6-cos-v1",
            "all-mpnet-base-v2",
            "Muennighoff/SGPT-1.3B-weightedmean-msmarco-specb-bitfit"
        ]

        super().__init__(options, is_leaf, is_root)