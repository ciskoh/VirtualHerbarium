""" Module to scrape wikipedia using wikipedia wikipediaapi"""

from utils import *
import wikipediaapi as wikip


#------------------Classes

class wikiTextContainer(TextContainer):
    """class holding text and data from each website"""

    def webscrapeWikipedia(self):
        """wrapping function to scrape wikipedia"""
        self.checkForMainAttr()
        if self.journalName == 'wikipedia':
            self.wikiPage = self.buildWikiPage(self.plantName)

            wikiOnlineTitles = [i.title for i in page_py.section]
            contentsDict= [self.wikipage[self.wikiOnlineTitles.index(i)] for i in self.sectionsTitle  ]
            # for i in self.sectionTitles:
            #     wikiSecIndex = sectionsTitle.index(i)
            #     contentsDict[i] = page_py.sections[index]
            # self.sectionContents = contentsDict

    def checkForMainAttr(self, attrList=wikiTitles):
        """checks for main attributes before scraping webpage"""
        for i in attrList:
            assert(getattr(self, i)), f"{i} is still missing, cannot scrape wikipedia"

    def buildWikiPage(self, plantName):
        """build wikipage using wikip. api with checks"""
        wiki_wiki = wiki.Wikipedia('en')
        page_py = wiki_wiki.page(plantName)
        if page_py.exists():
            print(page_py)
            return page_py
        else:
            self.wikiPage=False
            print(f'could not find wikipediaPage for {plantName}')


if __name__ == "__main__":
    test  =wikiTextContainer("wikipedia", 'name1 name2', ["aa", "bb", "cc"])
print(test.__dict__)
dir(test)
self=test.checkForMainAttr()
