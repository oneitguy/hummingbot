from unittest import TestCase

from hummingbot.connector.exchange.bitoreum.bitoreum_order_book import BitoreumOrderBook
from hummingbot.core.data_type.order_book_message import OrderBookMessageType


class BitoreumOrderBookTests(TestCase):

    def test_trade_message_from_exchange(self):
        example_time = 1234567890

        example_trade = {
            "date": 1234567899,
            "tid": '3333',
            "taker_type": "buy",
            "price": 8772.05,
            "amount": 0.1,
        }
        message = BitoreumOrderBook.trade_message_from_exchange(example_trade,
                                                                  example_time,
                                                                  metadata={"trading_pair": "BTC-USDT"})

        self.assertEqual(OrderBookMessageType.TRADE, message.type)
        self.assertEqual(1234567890, message.timestamp)
        self.assertEqual("BTC-USDT", message.content["trading_pair"])
        self.assertEqual(8772.05, message.content["price"])
        self.assertEqual(0.1, message.content["amount"])
        self.assertEqual(1.0, message.content["trade_type"])
