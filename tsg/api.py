import requests
import json


class Api(object):
    def __init__(self):
        self.__headers ={}


    def set_header(self, token):
        self.__headers['Authorization'] = 'Token %s' % (token)

    def _req(self, url):
        return requests.get(url, headers=self.__headers).text

    def get_tsg_index(self):
        self.tsg_index = None
        if self.tsg_index is None:
            self.tsg_index = json.loads(self._req("https://www.thesharegame.com/api/tsgindex/"))
        return self.tsg_index

    def get_your_depot(self):
        self.your_depot = None
        if self.your_depot is None:
            self.your_depot = json.loads(self._req("https://www.thesharegame.com/api/your/depot/"))
        return self.your_depot

    def get_your_buys(self):
        self.your_buys = None
        if self.your_buys is None:
            self.your_buys = json.loads(self._req("https://www.thesharegame.com/api/your/buy/"))
        return self.your_buys

    def get_your_sells(self):
        self.your_sells = None
        if self.your_sells is None:
            self.your_sells = json.loads(self._req("https://www.thesharegame.com/api/your/sell/"))
        return self.your_sells

    def get_share(self, id):
        self.share = None
        if self.share is None:
            self.share = json.loads(self._req("https://www.thesharegame.com/api/share/" + str(id) + "/"))
        return self.share

    # Error: 504 Gateway time-out
    def get_share_depot(self, id):
        self.share_depot = None
        if self.share_depot is None:
            self.share_depot = json.loads(self._req("https://www.thesharegame.com/api/share/"+ str(id) +"/depot/"))
        return self.share_depot

    def get_buy_share(self, id):
        self.buy_share = None
        if self.buy_share is None:
            self.buy_share = json.loads(self._req("https://www.thesharegame.com/api/buy/of_share/" + str(id) +"/"))
        return self.buy_share

    def get_sell_share(self, id):
        self.sell_share = None
        if self.sell_share is None:
            self.sell_share = json.loads(self._req("https://www.thesharegame.com/api/sell/of_share/" + str(id) +"/"))
        return self.sell_share

    def get_bond_credit_statistics(self):
        """This function returns HTML and no JSON object"""
        return self._req("https://www.thesharegame.com/bond/credits/statistics/")