from krakenex import API
from socket import timeout


class CurrencyPair(object):
    def __init__(self, pair_str):
        self.pair = pair_str
        self.api = API()

    def get_bidask(self, count=1):
        temp2 = True
        while (temp2):
            temp = self.api.query_public("Depth", {"pair": self.pair, "count": count})
            if len(temp["error"]) == 0:
                temp2 = False
                return float(temp["result"][self.pair]["bids"][0][0]) / (1.0026), float(temp["result"][self.pair]["asks"][0][0]) * (1.0026)

class CurrencyPairs(object):
    def __init__(self, pairs_arr, logging, fee_pct, fee_offset_pct):
        self.pairs = pairs_arr
        self.api = API()
        self.fee_multiplier = (1 + (fee_pct + fee_offset_pct)/100)
        self.logging = logging
        self.logging.info("CurrencyPairs object created")
        print (self.fee_multiplier)

    def get_bidasks(self):
        temp2 = True
        while (temp2):
            try:
                temp = self.api.query_public("Ticker", {"pair": self.pairs})
                if len(temp["error"]) == 0:
                    temp2 = False
                    eth_usd_b, eth_usd_a = temp["result"]["XETHZUSD"]['b'][0] , temp["result"]["XETHZUSD"]['a'][0]
                    xbt_usd_b, xbt_usd_a = temp["result"]["XXBTZUSD"]['b'][0] , temp["result"]["XXBTZUSD"]['a'][0]
                    eth_xbt_b, eth_xbt_a = temp["result"]["XETHXXBT"]['b'][0] , temp["result"]["XETHXXBT"]['a'][0]

                    self.logging.info("-------------------------------------------")
                    self.logging.info("ETH_USD: " + eth_usd_b + " @ " + eth_usd_a)
                    self.logging.info("XBT_USD: " + xbt_usd_b + " @ " + xbt_usd_a)
                    self.logging.info("ETH_XBT: " + eth_xbt_b + " @ " + eth_xbt_a)
                    self.logging.info("-------------------------------------------")

                    return float(eth_usd_b) / self.fee_multiplier, 1.0 / (float(eth_usd_a) * self.fee_multiplier), \
                           float(xbt_usd_b) / self.fee_multiplier, 1.0 / (float(xbt_usd_a) * self.fee_multiplier), \
                           float(eth_xbt_b)/ self.fee_multiplier, 1.0 / (float(eth_xbt_a) * self.fee_multiplier), \

            except timeout:
                print ("Timeout Error")
            except ValueError:
                print ("JSON Decode Error")


if __name__=="__main__":
    pairs = "XETHZUSD,XXBTZUSD,XETHXXBT"
    test = CurrencyPairs(pairs)
    print (test.get_bidasks())















