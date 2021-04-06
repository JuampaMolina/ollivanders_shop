from domain.types import *

class Factory:

    @staticmethod
    def createItemObject(item):
        classesDicctionary = {
            "Sulfuras, Hand of Ragnaros": "Sulfuras",
            "Aged Brie": "AgedBrie",
            "Backstage passes to a TAFKAL80ETC concert": "Backstage",
            "Conjured Mana Cake": "ConjuredItem",
            "+5 Dexterity Vest": "ConjuredItem",
            "Normal Item": "NormalItem"
        }
        try:
            itemClass = classesDicctionary[item[0]]
        except KeyError:
            itemClass = classesDicctionary["Normal Item"]
        finally:
            return eval(itemClass + str(tuple(item)))
