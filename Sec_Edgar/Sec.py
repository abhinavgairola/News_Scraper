import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import os
#from google.colab import drive
class Sec_Master:
    """"
    Functions to extract CIK number and Master files 
    from SEC database.
    """
    def __init__(self):
         
         return None 
    def CIK_extracter(self,TKS,payload_):
        URL = 'http://www.sec.gov/cgi-bin/browse-edgar?'
        CIK = re.compile(r'CIK=(\d\d\d\d\d\d\d\d\d\d)')
        CIK_number = {}
        for tickers in TKS:
            #print("This is URL {}".format(URL))
            payload_['CIK']=tickers
            #print("This is payload {} ".format(payload))
            html_doc=requests.post(URL, params=payload_).text#requests.get(URL.format(tickers)).text
            print(requests.post(URL, params=payload_).url)
            #print(help(requests.get(URL.format(tickers)).content))
            soup = BeautifulSoup(html_doc, 'html.parser')
            for link in (soup.findAll('a')):
                results= (re.findall(CIK,link.get('href')))
                if results:
                    CIK_number[tickers]=(results[0])


        print(CIK_number)
        return CIK_number

    def url_generator(self,base_url,comp):
        url = base_url
        for r in comp:
            url = '{}/{}'.format(url,r)
        return url



if __name__ == "__main__":
    Obj=Sec_Master()
    Tech_Tickers = ['goog', 'aapl','amzn','msft','FB','NVDA','YELP']
    payload = {'CIK': None, 'Find': 'Search','owner':'exclude','action':'getcompany'}
    CIK_ticks_mapping = Obj.CIK_extracter(Tech_Tickers,payload)
    CIK_df = pd.DataFrame(CIK_ticks_mapping,index=[0])
    CIK_df_T = CIK_df.T.reset_index().rename(columns={'index':'Tickers',0:'CIK'})
    base_url = r'https://www.sec.gov/Archives/edgar/daily-index'
    year= '2019'
    url = Obj.url_generator(base_url, [year, 'index.json'])
    print(url)
    print(CIK_df_T)
    