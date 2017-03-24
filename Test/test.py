from neo import Neo_Engine
import urllib
from bs4 import BeautifulSoup

def Get_Test_Data():
    data_file = file("test.csv","w")
    f = urllib.urlopen("https://www.cleartrip.com/trains/list")
    soup = BeautifulSoup(f,"html.parser")
    table = soup.body.table
    l = table.get_text().split("\n")
    if len(l)==0:
        raise ValueError
    try:
        while(1):
            l.remove("")
    except:
        pass
    header = l[:4]
    data_file.write(",".join(header))
    data_file.write("\n")
    for i in xrange(4,len(l),4):
        data_file.write(",".join(l[i:i+4]))
        data_file.write("\n")
    data_file.close()

if __name__=="__main__":
    obj = Neo_Engine()
    obj.getdata_and_train(121)
    obj.predict_delay(121)
