import pandas as pd 
import numpy as np 
import datetime 
from Price_data_handler import Price_data_handler
from Datetime_wrapper import Datetime_wrapper
import schedule
import time

class Price_data_recorder():
    
    def __init__(self) -> None:
        self.price_data_handler = Price_data_handler()
        self.datetime_wrapper = Datetime_wrapper()
        self.symbol = "^N225"
    
    def change_target(self,target_symbol):
        self.symbol = target_symbol

    def check_target(self):
        return self.symbol
    
    def get_latest_price(self):
        self.price_data_handler.get_current_price(self.symbol)

    def get_data(self):
        current_price = self.get_latest_price()
        current_time = self.datetime_wrapper.get_current_time()
        return current_price, current_time
    def record_price(self):
        current_price,current_time = self.get_data()
        current_time_str= self.datetime_wrapper.datetime_to_str(current_time)
        print(current_time_str)
        
    def start_recording(self):
        self.get_latest_price()
        schedule.every(1).seconds.do(self.record_price)
        while True:
            schedule.run_pending()
            time.sleep(0.1)
            


if __name__ == "__main__":
    price_data_recorder = Price_data_recorder()
    price_data_recorder.start_recording() 