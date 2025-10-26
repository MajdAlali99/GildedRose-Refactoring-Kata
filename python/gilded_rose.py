# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue # legendary

            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_pass(item)
            elif item.name.startswith("Conjured"):
                self._update_conjured_item(item)
            else:
                self._update_normal_item(item)

            item.sell_in = item.sell_in - 1 # decrease sell_in
     
            if item.sell_in < 0:
                self._update_expired_item(item)

    def _update_aged_brie(self, item):
        self._increase_quality(item)

    def _update_backstage_pass(self, item):
        self._increase_quality(item) # increase by 1
        if item.sell_in < 11:
            self._increase_quality(item) # increase by 2 (1+1)
        if item.sell_in < 6:
            self._increase_quality(item) # increase by 3 (1+1+1)

    def _update_conjured_item(self, item):
        self._decrease_quality(item, amount=2)

    def _update_normal_item(self, item):
        self._decrease_quality(item, amount=1)

    def _update_expired_item(self, item):
        if item.name == "Aged Brie":
            self._increase_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0       
        elif item.name.startswith("Conjured"):
            self._decrease_quality(item, 2)
        else: # for rest of items
            self._decrease_quality(item, 1)

    def _increase_quality(self, item):
        item.quality = min(50, item.quality + 1)

    def _decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
