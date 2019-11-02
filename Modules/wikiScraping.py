""" Module to scrape wikipedia using wikipedia wikipediaapi"""

from utils import TextContainer
from utils import wikiSectionTitles
import wikipediaapi as wiki


# ------------------Classes

class wikiTextContainer(TextContainer):
    """class holding text and data from each website"""
    

    def __str__(self):
        attrDict = str(self.__dict__)
        return f'wiki TextContainer object named {self.journalName} with the following attributes {attrDict}'

    def webscrapeWikipedia(self):
        """wrapping function to scrape wikipedia"""
        self.checkForMainAttr()
        if self.journalName == 'wikipedia':
            self.wikiPage = self.buildWikiPage(self.plantName)
            self.sectionContents = self.getWikiSections()
            if "Summary" in self.sectionTitles:
                self.sectionContents["Summary"] = self.wikiPage.summary
            else:
                pass
        else:
            print("journal is not wikipedia")


    def buildWikiPage(self, plantName):
        """build wikipage using wikip. api with checks"""
        plantName= self.plantName
        wiki_wiki = wiki.Wikipedia('en')
        page_py = wiki_wiki.page(plantName)
        if page_py.exists():
            return page_py
        else:
            print(f'could not find wikipediaPage for {plantName}')
            return False

    def getWikiSections(self):
        """extract specific section from wiki page"""
        wikiOnlineSections = [i for i in self.wikiPage.sections if i.title.title() in self.sectionTitles]
        dic = {}
        for v in wikiOnlineSections:
            k = v.title
            dic[k] = v.text
        return dic

if __name__ == "__main__":
    test = wikiTextContainer("wikipedia", 'Parthenium', wikiSectionTitles)
    print(test.__dict__)
    test.webscrapeWikipedia()
    print(test.sectionContents)
    print(test)
