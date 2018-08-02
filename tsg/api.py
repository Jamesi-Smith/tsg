import requests


class Api(object):
    def __init__(self):
        self.__headers ={}

    def set_header(self, token):
        self.__headers['Authorization'] = 'Token %s' % (token)

    def _req(self, url):
        return requests.get(url, headers=self.__headers).text

    def tsg_index(self):
        return self._req("https://www.thesharegame.com/api/tsgindex/")

    def your_depot(self):
        return self._req("https://www.thesharegame.com/api/your/depot/")

    def your_buy(self):
        return self._req("https://www.thesharegame.com/api/your/buy/")

    def your_sell(self):
        return self._req("https://www.thesharegame.com/api/your/sell/")

    def share(self, id):
        return self._req("https://www.thesharegame.com/api/share/" + str(id) + "/")

    # Error: 504 Gateway time-out
    def share_depot(self, id):
        return self._req("https://www.thesharegame.com/api/share/"+ str(id) +"/depot/")

    def buy_share(self, id):
        return self._req("https://www.thesharegame.com/api/buy/of_share/" + str(id) +"/")

    def sell_share(self, id):
        return self._req("https://www.thesharegame.com/api/sell/of_share/" + str(id) +"/")

    def bond_credit_statistics(self):
        """This function returns HTML and no JSON object"""
        return self._req("https://www.thesharegame.com/bond/credits/statistics/")