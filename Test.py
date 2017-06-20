from CurrencyPair import CurrencyPairs
import logging

def GetAllBidAsk(ethusd, xbtusd, ethxbt):
    eth_usd, usd_eth = ethusd.get_bidask()
    xbt_usd, usd_xbt = xbtusd.get_bidask()
    eth_xbt, xbt_eth = ethxbt.get_bidask()

    usd_eth, usd_xbt, xbt_eth = 1/usd_eth, 1/usd_xbt, 1/xbt_eth
    return eth_usd, usd_eth, xbt_usd, usd_xbt, eth_xbt, xbt_eth



def ArbitrageExists(eth_usd, usd_eth, xbt_usd, usd_xbt, eth_xbt, xbt_eth, logging):
    retVal = False
    if (eth_usd * usd_xbt * xbt_eth) > 1:
        print ("ETH_USD", eth_usd, "USD_XBT", usd_xbt, "XBT_ETH", xbt_eth)
        logging.info("ETH_USD,USD_XBT,XBT_ETH") #1
        retVal = True

    if (eth_xbt * xbt_usd * usd_eth) > 1:
        print ("ETH_XBT", eth_xbt, "XBT_USD", xbt_usd, "USD_ETH", usd_eth)
        logging.info("ETH_XBT,XBT_USD,USD_ETH") #2
        retVal = True

    if (xbt_usd * usd_eth * eth_xbt) > 1:
        print ("XBT_USD", xbt_usd, "USD_ETH", usd_eth, "ETH_XBT", eth_xbt)
        logging.info("XBT_USD,USD_ETH,ETH_XBT") #2
        retVal = True

    if (xbt_eth * eth_usd * usd_xbt) > 1:
        print ("XBT_ETH", xbt_eth, "ETH_USD", eth_usd, "USD_XBT", usd_xbt)
        logging.info("XBT_ETH,ETH_USD,USD_XBT") #3
        retVal = True

    if (usd_xbt * xbt_eth * eth_usd) > 1:
        print("USD_XBT", usd_xbt, "XBT_ETH", xbt_eth, "ETH_USD", eth_usd)
        logging.info("USD_XBT,XBT_ETH,ETH_USD") #1
        retVal = True

    if (usd_eth * eth_xbt * xbt_usd) > 1:
        print("USD_ETH", usd_eth, "ETH_XBT", eth_xbt, "XBT_USD", xbt_usd)
        logging.info("USD_ETH,ETH_XBT,XBT_USD") #2
        retVal = True

    return retVal

if __name__ == "__main__":
    pairs = "XETHZUSD,XXBTZUSD,XETHXXBT"
    logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
    test = CurrencyPairs(pairs, logging, fee_pct= 0.26, fee_offset_pct=-0.26)


    while (True):
        ArbitrageExists(*test.get_bidasks(), logging)





