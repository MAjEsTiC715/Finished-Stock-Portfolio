#========================================================  Documentation  ==================================================================================
#First, you will need to add the following function:
#GetSale - Finds the maximum expected value of selling a stock. The expected sale value of a stock is the current profit minus the future value of the stock:
    #Expected Sale value = ( ( Current Price - Buy Price ) - Risk * CurrentPrice ) * Shares
#The GetSale function should calculate this value for each stock in the portfolio, and return the stock symbol with the highest expected sale value.
#Change/update/add the main function. This should take no arguments, but present a menu item consisting of "1. Add Stock", "2. Recommend Sale" and "3. Exit".
#If the user selects '1,' the Add Stock function is called, and when it is complete, the menu is presented again.
#If the user selects '2,' the Symbol of the stock corresponding to the highest expected value
#(returned by GetSale) should be displayed, and the menu presented after completion. If the user selects '3', the program should end.
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.
#===========================================================================================================================================================

class CompanyStocks:


    #The __init__ method initializes the aruguments stockSym, comName, bPrice, cPrice, risk, shares, expectSale
    #all the self. attributes are asigned a name
    def __init__(self, stockSym, comName, bPrice, cPrice, risk, shares, expectSale):
        self.__stockSym = stockSym
        self.__comName = comName
        self.__bPrice = bPrice
        self.__cPrice = cPrice
        self.__risk = risk
        self.__shares = shares
        self.__expectSale = expectSale

    #The set_stockSym method sets the stockSym attribute
    def set_stockSym(self, stockSym):
        self.__stockSym = stockSym

    #The set_comName method sets the comName attribute
    def set_comName(self, comName):
        self.__comName = comName

    #The set_bPrice method sets the bPrice attribute
    def set_bPrice(self, bPrice):
        self.__bPrice = bPrice

    #The set_cPrice method sets the cPrice attribute
    def set_cPrice(self, cPrice):
        self.__cPrice = cPrice

    #The set_risk method sets the risk attribute
    def set_risk(self, risk):
        self.__risk = risk

    #The set_shares method sets the shares attribute
    def set_shares(self, shares):
        self.__shares = shares

    #The set_expectSale method sets the expectSale attribute
    def set_expectSale(self, expectSale):
        self.__expectSale = expectSale

    #The get_stockSym method returns the stockSym attribute
    def get_stockSym(self):
        return self.stockSym

    #The get_comName method returns the comName attribute
    def get_comName(self):
        return self.comName

    #The get_bPrice method returns the bPrice attribute
    def get_bPrice(self):
        return self.bPrice

    #The get_cPrice method returns the cPrice attribute
    def get_cPrice(self):
        return self.cPrice

    #The get_risk method returns the risk attribute
    def get_risk(self):
        return self.risk

    #The get_shares method returns the shares attribute
    def get_shares(self):
        return self.shares

    #The get_expectSale method returns the expectSale attribute
    def get_expectSale(self):
        return self.expectSale

    #The __str__ method returns the object's state as a string
    #Within the method we convert certain attributes into float form by using the format() method
    def __str__(self):
        return "\n--------------------------------------------------------------------------\n" + \
               "Company Symbol: " + self.__stockSym + "\n" + \
               "Company Names: " + self.__comName + "\n" + \
               "Companys BUY; " + format(self.__bPrice, '.2f') + "\n" + \
               "CURRENT price : " + format(self.__cPrice, '.2f') + "\n" + \
               "Companys RISK %: " + format(self.__risk, '.2f') + "\n" + \
               "SHARES bought : " + format(self.__shares, '.2f') + "\n" + \
               "Expected Sales Value: " + format(self.__expectSale, '.2f') + "\n" + \
               "--------------------------------------------------------------------------\n"









