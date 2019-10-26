#! /usr/bin/env python3
"""class definitions for VirtualHerbarium"""

class Plant:
    """Class for plant objects to be filled with text from the web"""

    type="plant"

    def __init__(self, name):
        self.name = name
        self.wikipedia: list = ["Summary", "Description", "Uses"]
