# HINT
**Team Matrix**

Neon is our prediction engine which will predict whether given train will be delayed or not in future.
It uses K nearest neighbors classifier to classify among two groups [0,2] ( 0 for delay, 1 for in time and 2 for before time).
We take last year data from internet by scrapping table using BeautifullSoup framework.


### How to Deploy?

#### Requirements
* django
* sklearn
* pandas
* bs4
* gspread

1. Change the present working directory to the downloaded repository.
2. Type the following commnads in the terminal 

`cd HintApp/`

`python manage.py runserver`

3. Now you can run the website by typing http://127.0.0.1:8000/ in the address bar of the browser.

### How to check result?

Navigate to http://127.0.0.1:8000/predict/ to check the result of the previous form filled.
