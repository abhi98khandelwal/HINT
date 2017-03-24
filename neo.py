import datetime
import random
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import get_online_data


class Neo_Engine:

    def __init__(self):
        self.clf = KNeighborsClassifier()
        #elf.regressor = LinearRegression()

    def getdata_and_train(self,train_no):
        get_online_data.Create_DataFile(train_no)
        df = pd.read_csv('data.csv')
        df.fillna(value=0, inplace=True)
        new_df = df.apply(LabelEncoder().fit_transform)
        X = new_df.drop(['Status'], axis=1)
        X = X.drop(['Reach Time'], axis=1)
        y = new_df['Status']
        self.clf.fit(X, y)

        # Train the model of particular locomotive
        # Example : Get train data from user. convert results to DataFrame and feed it.

    def predict_delay(self):
        X = preprocess_and_add_data()
        prediction = self.clf.predict(X)
        print(prediction)
        #based on training will predict delay of locomotive next day




def preprocess_and_add_data():
    df = pd.read_csv('data.csv')
    df.fillna(value=0, inplace=True)
    columns = df.columns.values
    index = 0
    for column in columns[1:2]:
        X = df[column]
        for i, x in enumerate(X):
            if x != 'Late' and x != 'Before':
                index = i
                break
    X = None
    for column in columns[:1]:
        X = df[column][index]
        break
    new_time = str(datetime.datetime.now())
    X = list(X)
    new_time = list(new_time)
    #print(X)
    #print(new_time)
    X[:11] = new_time[:11]
    X = "".join(X)
    data_dict = {
        'StartedOn':[X],
        'Delay':df['Delay'][random.randint(0,len(df))]
    }
    enc = LabelEncoder()
    new_df = pd.DataFrame(data=data_dict)
    new_df = new_df.apply((LabelEncoder().fit_transform))
    return new_df

if __name__=="__main__":
    p = Neo_Engine()
    p.getdata_and_train(12130)
    #print(p.predict_delay())


