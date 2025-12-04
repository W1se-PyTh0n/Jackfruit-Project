 CashCrabCruzers
Jackfruit Problem- Mini project (Python)
Our team:
Name	SRN	Class
Aarohi Gupta	PES1UG25 BT001	C1
Abhijith B Bharadwaj	PES1UG25EC008	C1
Aashmeen Kaur	PES1UG25CS010	C1
Abhiram Vinayak Shanbhag	PES1UG25EC012	C1
 
GitHub Link:  https://github.com/W1se-PyTh0n/Jackfruit-Project
Problem Statement:
Currency conversion using Forex API
With this project, we aimed to create an easy to use and rapid application to convert currencies across the globe.
Methodology/Approach:
Step 1: Importing different modules and API
We first import all the packages including requests  module which is used to send HTTPS GET request, datetime and timedelta used for obtaining dates for the last 7 days, customtkinter for the GUI to create easy widgets and matplotlib.pyplot to create the graph.
We are using two APIs in our code which consist of:
•	ExchangeRate API – has support for wide range of currencies and conversion rates but doesn’t give historical data
•	Frankfurter API – can provide historical data for the currency chart
 
Step 2: Creating a function to fetch currency codes of each country and its name. We also create another function which takes the base currency, target currency and an amount and query the API to get the converted amount
 
Step 3: After this we create the app. We use customTkinter for this purpose, creating the main window and adding in all the elements for a user friendly experience. We then add the heading, frames, buttons, drop down button.
 
Step 4: The user can enter the amount to convert, the base currency code and target currency (can be selected in the drop down menu or typed in). After hitting the convert button, the converted currency is displayed.
 
Step 5 : As an extra feature, we have added a functionality to plot a chart that compares two currency values. On pressing the “7-day Currency Comparison” button, it takes the user to a new window. They can select the currencies to be compared and the graph is created by mathplotlib using mplot.subplots()(This is placed in the window by using FigureCanvasTkAgg).
 
Step 6:  The required output of the converted amount and the comparison chart is displayed in seperate windows.
 
 
Data Structures used:
1) Lists – for storing currency codes and conversion values
2) Dictionary – The APIs used return a JSON(JavaScript Object Notation) file where data is stored in a dictionary.
3) Functions – Modular approach for conversion, querying the API for currency data, plotting charts
 
 
Challenges Faced:
 
We had to use two API’s as the ExchangeRate API didn’t provide us historical exchange rate for the currencies (for the currency chart) but had support for a large number of currencies for conversion. So we included the frankfurter API as well(which has support to a limited number of currencies but gave us the required historical data). Also the Frankfurter API didn't provide currency data during holidays. So we had to implement a logic to make sure we get 7 data points for plotting the graph.
 
Scope for improvement:
●	Show real-time graph comparing user selected currencies.
●	Being able to show real-time currency conversion rate in the currency converter window.
●	Converting the base currency to multiple target currencies at once.
●	Currently only 7 day historical trend is supported. But 1-month, 3-month or more historical trends can be included.

Sample Inputs and Outputs:
Main window: 
 

Currency Conversion:
 

 






Supported currencies for conversion:

 

 
 
 
 
 
 









Comparison chart:
 







Supported currencies for Comparison chart:
 


