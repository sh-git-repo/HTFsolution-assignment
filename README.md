# Limit Order Book for HTFsolution

## Table of contents
* [Introduction](#introduction)
* [Tutorial](#tutorial)
* [Dependencies](#dependencies)
* [Conclusion](#conclusion)

## Introduction
#### Technologies used
* The complete application was developed in Python 3.8.5

## Tutorial
#### Main console
* This is the main screen of the console application, here we have three options as per the given requirements.
* Market Orders
* Limit Orders
* Cancel particular order
* We will explore these options in depth.
```
25/09/2020 10:35:00
ASKS
----------------------------------------
Prize     Size

11.42   :   900
11.41   :   1400
11.4   :   1205
11.39   :   1600
11.38   :   400
----------------------------------------
----------------------------------------

25/09/2020 10:35:00
BIDS
----------------------------------------
Prize     Size

11.36   :   2700
11.35   :   1100
11.34   :   1100
11.33   :   1600
11.32   :   700
----------------------------------------
----------------------------------------

Enter 1 for Market orders
Enter 2 for Limit orders
Enter 3 to cancel a particular order
Enter any other key to exit
```

#### Market Orders
* Market Buy
* Here the user can choose to buy the commodity, the application will automatically buy the cheapeast available option.
```
Enter 1 for Market orders
Enter 2 for Limit orders
Enter 3 to cancel a particular order
Enter any other key to exit
>> 1
1 for Market Buy
2 for Market Sell
>> 1
Enter quantity
>> 500
```
* As you can observe 400 in quantity of the item with lowest price, '11.38', was completely bought, hence the application bought remaining 100
from the next lowest '11.39'
```
25/09/2020 11:31:38
ASKS
----------------------------------------
Prize     Size

11.42   :   900
11.41   :   1400
11.4   :   1205
11.39   :   1500.0  # <------ 1600 + 400 - 500
----------------------------------------
----------------------------------------
```
* Market Sell
```
1 for Market Buy
2 for Market Sell
>> 2
Enter quantity
>> 800
```
* As you can observe 800 in quantity of the item with highest price, '11.36', was sold.
```
25/09/2020 11:37:29
BIDS
----------------------------------------
Prize     Size

11.36   :   1900.0 # <---- 2700 - 800
11.35   :   1100
11.34   :   1100
11.33   :   1600
11.32   :   700
----------------------------------------
----------------------------------------
```
#### Limit Orders
* The Limit orders mimics the ordering as shown in '5-minute-finance'.
* Below is the showcase for limit buy for the price when limited to '11.38'.
```
Enter 1 for Market orders
Enter 2 for Limit orders
Enter 3 to cancel a particular order
Enter any other key to exit
>> 2
1 for Limit Buy
2 for Limit Sell
>> 1
Enter quantity, limit
>> 500 11.38

###############
###############

25/09/2020 11:45:59
ASKS
----------------------------------------
Prize     Size

11.42   :   900
11.41   :   1400
11.4   :   1205
11.39   :   1500.0 # <---- 1600 + 400 - 500
----------------------------------------
----------------------------------------
```
* Limit buy on price '11.37'.
* As the price doesn't exist in ASKS it is instead added to BIDS, same as per '5-minute-finance'.
```
1 for Limit Buy
2 for Limit Sell
>> 1
Enter quantity, limit
>> 900 11.37

##########
##########

25/09/2020 11:51:30
BIDS # <-----
----------------------------------------
Prize     Size

11.37   :   900.0 # <----
11.36   :   2700
11.35   :   1100
11.34   :   1100
11.33   :   1600
11.32   :   700
----------------------------------------
----------------------------------------
```
* Limit buy on price '11.36'.
* As the price doesn't exist in ASKS it is instead added to BIDS, same as per '5-minute-finance'.
```
1 for Limit Buy
2 for Limit Sell
>> 1
Enter quantity, limit
>> 1000 11.36

############
############

25/09/2020 11:58:27
BIDS
----------------------------------------
Prize     Size

11.37   :   900.0
11.36   :   3700.0 # <------
11.35   :   1100
11.34   :   1100
11.33   :   1600
11.32   :   700
----------------------------------------
----------------------------------------
```
* For the Limit sell orders, the functioning is same as per '5-minute-finance'.

#### Cancel a particular order
* A user can cancel(or restore) any particular order, note that cancelling an order does not only undo the changes of that particular order, but also resets the order book to the point it was before the transaction was made.
* This process creates temporary json files from which the book is reset back depending on the option, the files are deleted once the application is exited normally.
```
# BEFORE ORDER
25/09/2020 12:07:07
ASKS
----------------------------------------
Prize     Size

11.42   :   900
11.41   :   1400
11.4   :   1205
11.39   :   1600 # <-----
11.38   :   400 # <-----
----------------------------------------
----------------------------------------

##########
# MAKING MARKET ORDER
Enter 1 for Market orders
Enter 2 for Limit orders
Enter 3 to cancel a particular order
Enter any other key to exit
>> 1
1 for Market Buy
2 for Market Sell
>> 1
Enter quantity
>> 800
##########

########
# AFTER ORDER and BEFORE CANCELLATION
25/09/2020 12:08:26
ASKS
----------------------------------------
Prize     Size

11.42   :   900
11.41   :   1400
11.4   :   1205
11.39   :   1200.0 # <-------
----------------------------------------
----------------------------------------
########

######## Cancellation
Enter 1 for Market orders
Enter 2 for Limit orders
Enter 3 to cancel a particular order
Enter any other key to exit
>> 3
Warning, selecting any order to be cancelled will undo all the changes upto that order

Market Buy - 1
   800.0 None 25/09/2020 12:08:26

Market Sell - 2
   700.0 None 25/09/2020 12:14:17

Enter the order number to be undone
>> 1
##########

######## AFTER CANCELLING
25/09/2020 12:14:47
ASKS
----------------------------------------
Prize     Size

11.42   :   900
11.41   :   1400
11.4   :   1205
11.39   :   1600 # <---- restored
11.38   :   400 # <---- restored
----------------------------------------
----------------------------------------
```

## Conclusion
#### Thank you to everyone and anyone going through this submission.
Please Evaluate this assignment very leniently. I have tried my best to learn and implement a solution which satisfies the majority of the stated requirements, I know that this solution can be improved much more, therefore, I only ask you to give me chance to work at HFTSolution to prove that I am a person who is willing learn and grow and do whatever it takes to solve any problem that is thrown my way.

Finally, thanks a lot to everyone evaluating my submission.

Sincerely,

Shahbaz Ahmed Khan