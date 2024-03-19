from src.menus._menu import Menu
from src.menus.topic._topic import TopicMenu

class Landing(Menu):
    def __init__(self):
        is_root = True
        is_leaf = False
        options = [
            "Run a Topic Model",
            "Run an Optimization routine for a Topic Model (GPU reccomended)",
            "Load Global Data",
            "Load Global Topic Model Configuration",
            "Load Global Optimization Configuration",
        ]
        super().__init__(options, is_leaf, is_root)

        menus = [
            TopicMenu(),
            None,
            None,
            None,
            None
        ]
        self._map_options_to_menus(options, menus)
