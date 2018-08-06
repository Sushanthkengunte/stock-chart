# stock-chart

Stock Chart:

Build a single web page stock chart. 

Designed the program adhering to MVC architecture. 

Technologies used are:

              •	Python
              
              •	Flask
              
              •	D3
              
              •	JavaScript
              
              •	JQuery
              
              •	 Html
              
              •	Bootstrap
              
              •	ajax. 
              
Model: (Model.py)

	Data can be 
  
              •	extracted from a given company with quandl code
              
              •	filtered out for a range of years
              
              •	used to get the required category of stock prices (Open,close, etc)
              
              •	used to calculate moving average of a list considering a factor of previous values
              
              •	used to creates label to display
              
View: (baseTemplate.html, index.html)

              •	Provides a "stock prices" home screen logo
              
              •	Uses radio buttons to list the different companies from which we can choose
              
              •	Two text inputs to take years
              
              •	A submit button to generate the stock chart
              
              •	Reset button to reset the page
              
              •	A loading bar showing that its loading not crashed
              
              •	Chart which is displayed
              
Controller: (stockPrices.py)

              •	It defines the routes
              
              •	“/” is the root directory when http makes a get request on it,its redirected to index method displaying elements in index.html
              
              •	“/stockchart” when the http makes a post request to it a chart is generated and displayed.
              
              •	Uses the model.py to get the data, process the obtained data and generate graph
              
              •	Sends it to the View to be displayed.


Error handling and Testing:

              •	Tested the case when api returns an error
              
              •	Performed unit testing on filtering and calculating moving average
              
              •	Performs client-side validation on the years specified
              
Required Libraries:

              •	Flask
              
              •	Mpld3
              
              •	Matplotlib
              
              •	Unittest
              
              •	Numpy
              
              •	Pandas
              
              •	Threading
              
              •	Datetime
              
              •	Quandl
              
              •	Json
              
Running the script

            •	Run the controller script, stockPrices.py
            
            •	Open “http://localhost:7777”
            
            •	Add quandl key in Model.py file
            


