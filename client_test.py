import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            expected_price = (bid_price + ask_price) / 2
            self.assertEqual(price, expected_price, f"Expected price {expected_price} for stock {stock}, but got {price}")

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            expected_price = (bid_price + ask_price) / 2
            self.assertEqual(price, expected_price, f"Expected price {expected_price} for stock {stock}, but got {price}")

    """ ------------ Add more unit tests ------------ """
    # Example additional test:
    def test_getRatio(self):
        self.assertEqual(getRatio(10, 5), 2)
        self.assertEqual(getRatio(5, 10), 0.5)
        self.assertIsNone(getRatio(10, 0))  # Expecting None when dividing by zero

if __name__ == '__main__':
    unittest.main()
