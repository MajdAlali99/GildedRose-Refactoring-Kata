# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_item_degrades(self):
        items = [Item("foo", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 9)

    def test_conjured_degrades(self): 
        items = [Item("Conjured Whatever", 3, 6)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 4) # twice as fast

    def test_aged_brie_degrades(self): 
        items = [Item("Aged Brie", 2, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 1) # increases in quality

    def test_never_negative(self):
        items = [Item("foo", 0, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)

        
if __name__ == '__main__':
    unittest.main()
