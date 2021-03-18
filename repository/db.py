class DB:
    """inventario = [
        ["+5 Dexterity Vest", 10, 20],
        ["Aged Brie", 2, 0],
        ["Elixir of the Mongoose", 5, 7],
        ["Sulfuras, Hand of Ragnaros", 0, 80],
        ["Sulfuras, Hand of Ragnaros", -1, 80],
        ["Backstage passes to a TAFKAL80ETC concert", 15, 20],
        ["Backstage passes to a TAFKAL80ETC concert", 10, 49],
        ["Backstage passes to a TAFKAL80ETC concert", 5, 49]
    ]"""

    inventory = [
        {
            "name": "+5 Dexterity Vest",
            "sell_in": 10,
            "quality": 20
        },
        {
            "name": "Aged Brie",
            "sell_in": 2,
            "quality": 0
        },
        {
            "name": "Aged Brie",
            "sell_in": 5,
            "quality": 2
        },
        {
            "name": "+5 Dexterity Vest",
            "sell_in": 8,
            "quality": 34
        }
    ]

    @staticmethod
    def get_item(name):
        items = DB.inventory
        return [item for item in items if item["name"] == name]