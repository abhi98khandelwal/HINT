from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import urllib.error
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

"""
base_url = 'http://runningstatus.in/history'
train_no = str(input("Enter Train No."))
querr = {'querry':train_no}
querr = urllib.parse.urlencode(querr)
url = '/'.join([base_url,querr])
response = urllib.request.urlopen(url)
html_bytes = response.read()
html= html_bytes.decode('utf-8')
soup = BeautifulSoup(html,'html.parser')

class Neo_Engine:

    def __int__(self):
        self.clf = LinearRegression()

    def getdata(self,df):
        # Train the model of particular locomotive
        # Example : Get train data from user. convert results to DataFrame and feed it.
        pass

    def predict_delay(self):
        #based on training will predict delay of locomotive next day
"""


df = pd.read_csv('data.csv')
df.fillna(value=0,inplace=True)
new_df = df.drop(['Status'],axis=1)
#new_df = new_df.drop(['ReachTime'],axis=1)

new_df = new_df.apply(LabelEncoder().fit_transform)

X = new_df.drop(['Delay'],axis=1)
y = new_df['Delay']

print(new_df)
