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

import re #import the 're' library
import CompanyStocks #import the class 'CompanyStocks'

run = True #establish run as a global variable


#========================================================  main() function ========================================================================================
#define main() as a function
    #call global variable 'add' and 'run'
    #The while loop allows us to control how long to run the function with 'run' being our sentinel
        #establish a try catch method
            #establish a local variable 'mode' and set it to 0
            #establish 'mode' as a user int(input() asking what type of function he/she would like to run
            #we use multiple 'if' statements to deteremine which function the user wants to run
            #if 'mode' is 1 then it runs the first function being 'addStock(mystocks)'
                
            #if 'mode' is 2 then it runs the second function being 'findStock(mystocks)'
            
            #if 'mode' is 3 then it exits and asks the user to hit ENTER to exit
            #else: if the user does not enter any one of these numbers then they are prompted to enter a number between 1 and 3
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================


def main():
    global run
    global add

    stocks_dct = {}
    mystocks = stocks_dct

    while run == True:
        try:
            mode = 0
            mode = int(input('\nPlease select what function to test\n\n(1)'
                               ' Add Stock.'
                               '\n\n(2) Find Stock.\n\n'
                               '(3) Exit\n\n---------------------------------'
                               '-----------------------------------------\n:'))
            
            if mode == 1:
                addStock(mystocks)
            if mode == 2:
                findStock(mystocks)
            if mode == 3:
                input('Exit\nPress enter to exit.')
                run = False
            else:
                print ('You Need To Enter A Number Between 1 and 3')

        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')


#========================================================  addStock(mystocks) Function  ==================================================================================
#define addStock(mystocks) as a function
    #establish a try catch method
        #get user input for the companys stock symbol using 'stockSym'
        #re.match checks for lower and upper case letters for 'stockSym'
            #if true then ask for users input for the companys name (else print an error and restart the function)
            #repeat re.match
                #if true then ask for user for next input
                    #if the user enters a number >= 0 then proceed (else: display that input needs to be positive and restart function)
                        #if the user enters a number >= 0 then proceed (else: display that input needs to be positive and restart function)
                            #if the user enters a number >= 0 and <= 100 then proceed (else: display that input needs to be positive and restart function)
                                #if the user enters a number >= 0 then proceed (else: display that input needs to be positive and restart function)
                                    #set 'expectSale as an argument for the function 'GetSale()'
                                    #set 'entry' as an argument and add to the class 'CompanyStocks' under 'CompanyStocks' and add those other arguments
                                    #if 'stockSym' is not in mystocks then proceed to add 'entry' to the list under 'stockSym'
                                    #else say that it has been entered
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================


def addStock(mystocks):
    try:
        stockSym = input('Enter your companys stock symbol: ')
        if re.match("^[a-zA-Z\s]*$", stockSym):
            comName = input('Enter your companys name: ')
            if re.match("^[a-zA-Z\s]*$", comName):
                bPrice = float(input('Enter a buy price for your companys stock: '))
                if bPrice >= 0:
                    cPrice = float(input('Enter current price for your companys stock: '))
                    if cPrice >= 0:
                        risk = float(input('Enter your risk percentage as an integer: '))
                        if risk >= 0 and risk <= 100:
                            shares = float(input('Enter the amount of shares you would like: '))
                            if shares >= 0:
                                expectSale = getSale(stockSym, comName, bPrice, cPrice, risk, shares)

                                entry = CompanyStocks.CompanyStocks(stockSym, comName, bPrice, cPrice, risk, shares, expectSale)


                                if stockSym not in mystocks:
                                    mystocks[stockSym] = entry
                                    print ('The entry has been added.')
                                else:
                                    print ('That Stock Symbol already exists')

                            else:
                                print ('Enter a Positive Integer')
                                print ('\n--------------------------------------------------------------------------\n')
                                addStock(mystocks)
                        else:
                            print ('You need to enter a percentage between 0 and 100')
                            print ('\n--------------------------------------------------------------------------\n')
                            addStock(mystocks)
                    else:
                        print ('Enter a Positive Integer')
                        print ('\n--------------------------------------------------------------------------\n')
                        addStock(mystocks)
                else:
                    print ('Enter a Positive Integer')
                    print ('\n--------------------------------------------------------------------------\n')
                    addStock(mystocks)
            else:
                print ("Error! Only letters a-z allowed!")
                print ('\n--------------------------------------------------------------------------\n')
                addStock(mystocks)
        else:
            print ("Error! Only letters a-z allowed!")
            print ('\n--------------------------------------------------------------------------\n')
            addStock(mystocks)
            
    except ValueError:
        print ('That is not a valid input')
    except UnboundLocalError:
        print ('That is not a valid input')


#========================================================  findStock(mystocks) Function  ==================================================================================
#define findStock(mystocks) as a function
    #get user input for the companys stock symbol using 'stockSym'
    #re.match checks for lower and upper case letters for 'stockSym'
        #if true then use a .get function to get all items from mystocks
        #else print an error and restart the function
#===========================================================================================================================================================


def findStock(mystocks):

    stockSym = input('Enter the Stock Symbol of company to pull up the data: ')
    if re.match("^[a-zA-Z\s]*$", stockSym):
        print (mystocks.get(stockSym, 'That stock is not found'))
    else:
        print ("Error! Only letters a-z allowed!")
        findStock(mystocks)


#========================================================  getSale(stockSym, comName, bPrice, cPrice, risk, shares) Function  ==================================================================================
#define getSale(stockSym, comName, bPrice, cPrice, risk, shares) as a function
    #set 'expectSale as an argument to calculate the expected value sale
    #return that value from expectSale
#===========================================================================================================================================================


def getSale(stockSym, comName, bPrice, cPrice, risk, shares):
    expectSale = ((cPrice - bPrice) - risk/100 * cPrice) * shares
    return expectSale

#executes the entire program    
main()
