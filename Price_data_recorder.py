import pandas as pd 
import numpy as np 
import datetime 
from Price_data_handler import Price_data_handler
class Price_data_recorder():
    
    def __init__(self) -> None:
        self.price_data_handler = Price_data_handler()
        self.symbol = "^N225"
    
    def change_target(self,target_symbol):
        self.symbol = target_symbol

    def check_target(self):
        return self.symbol
    
    def get_latest_price(self):
        self.price_data_handler.get_current_price(self.symbol)

    def start_recording(self):
        self.get_latest_price()
        pass 


if __name__ == "__main__":
    price_data_recorder = Price_data_recorder()
    price_data_recorder.start_recording() 