from datetime import datetime

class Datetime_wrapper():
    def __init__(self) -> None:
        self.format = '%Y-%m-%d %H:%M:%S'
    
    def get_current_time(self):
        return datetime.now()

    def datetime_to_str(self,date:datetime):
        return date.strftime(self.format)
    
    def str_to_datetime(self,string:str):
        return datetime.strptime(string, self.format)