import requests

class Info:

    def __init__(self):
        return

##############################################################################################################################################
##############################################################################################################################################

    def get_summary(self, symbol, stock_url):

        # Get the summary of the latest articles by requesting the information using the concatenation of the stock's url and symbol

        try:

            response = requests.get(stock_url + symbol + '/news/last/1?token=pk_68f139eed0504ab5bd51bf9bb56a8526')
            json = response.json()
            return json[0]['summary']

        except Exception as e:

            print("Error in the Info class: " + str(e))

##############################################################################################################################################
##############################################################################################################################################

    def get_articles(self, symbol, stock_url):

        # Get the latest articles

        try:

            response = requests.get(stock_url + symbol + '/news/last/1?token=pk_68f139eed0504ab5bd51bf9bb56a8526')
            json = response.json()
            return json[0]['url']

        except Exception as e:

            print("Error in the Info class: " + str(e))

##############################################################################################################################################
##############################################################################################################################################

    def get_company_name(self, symbol, stock_url):

        # Get the company's name

        try:

            response = requests.get(stock_url + symbol + '/company?token=pk_68f139eed0504ab5bd51bf9bb56a8526')
            json = response.json()
            return json['companyName']

        except Exception as e:

            print("Error in the Info class: " + str(e))

##############################################################################################################################################
##############################################################################################################################################

    def get_exchange(self, symbol, stock_url):

        # Get exchange the stock belongs to

        try:

            response = requests.get(stock_url + symbol + '/company?token=pk_68f139eed0504ab5bd51bf9bb56a8526')
            json = response.json()
            return json['exchange']

        except Exception as e:

            print("Error in the Info class: " + str(e))