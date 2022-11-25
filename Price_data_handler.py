import pandas_datareader as pdr
import pandas as pd
from datetime import date,timedelta,datetime
import time
from matplotlib import pyplot as plt
from typing import List, Dict
import os 
class Price_data_handler():
    
    def __init__(self) -> None:
        pass
    
    def get_current_price(self, symbol:str, logout:bool = True):
        today = date.today()
        yesterday = today - timedelta(days=1)
        price_data = pdr.get_data_yahoo([symbol], 
                          start=yesterday, 
                          end=today)['Close']
        price = round(price_data[symbol][-1],3)
        if logout:
            print("The latest {} price : {}".format(symbol, price))
        return price