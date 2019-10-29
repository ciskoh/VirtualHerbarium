#! /usr/bin/env python3
"""class definitions for VirtualHerbarium"""

# ----------Settings-----------

import datetime
import wikipediaapi as wiki

# ---------Code----------------


class Plant:
    """Class for plant objects to be filled with text from the web"""

    type = "plant"

    def __init__(self, nameOrDic=None):
        if type(nameOrDic) is dict:
            for k, v in nameOrDic.items():
                setattr(self, k, v)
            print("added attributes from dictionary: %s" % self.__dict__)
            key, value = next(iter(nameOrDic.items()))
            self.name = value
            # TODO: add checks to name Variable as property?
        elif type(nameOrDic) is str:
            self.name = nameOrDic
            # TODO: add checks to name Variable as property?
        else:
            self.name = "name not defined"

    def __str__(self):
        attrDict = str(self.__dict__)
        return f'plant object named {self.name} with the following attributes {attrDict}'





if __name__ == "__main__":
    # class Plant tests
    print("test with object from str " + Plant('testClassPlant').__str__())
    tDic = {"rer": "balbla", "der": 2}
    print("test with object from dict " + Plant(tDic).__str__())
    print("test with no inputs " + Plant().__str__())

    # class TextContainer
    tSecs = ["aa", "bb", "cc"]
    test3 = TextContainer("wikipedia", "Lablab purpureus", tSecs)
    test3.__dict__
    plantName="dddurpureus"
    test3.webscrapeWikipedia()
    print(test3.wikiPage)

    plantName=
