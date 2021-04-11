import os
import time
import datetime
from os import path
import pandas as pd
from nsetools import Nse
from .df_param import get_df
from nsepy import get_history
nse=Nse()

def write_in_file(file,data):
    try:
        f = open(file,"w")
        
        for d in data:
            f.write(d)
        f.close()
        return 0
    except:
        print("Error in write_in_file")
        return -1

def get_all_codes():
    import  nsepy 
    from nsepy.symbols import get_symbol_list
    try:
        all = get_symbol_list()
        all.columns = [c.replace(' ', '_') for c in all.columns]
        all.to_csv('all_codes.csv', index=False)
    except:
        print("Unable to get codes, check your internet connection")

def date_of_listing(symbol):
    try:
        df = pd.read_csv('all_codes.csv')
        for i in range(len(df)):
            if df.SYMBOL[i] == symbol:
                print(df.SYMBOL[i], df._DATE_OF_LISTING[i])
                return df._DATE_OF_LISTING[i]
    except Exception as x:
        print(x)
        print("Unable to get listing date")
        print("downloading listing dates")
        get_all_codes()
        return date_of_listing(symbol)
        

#date_of_listing('20MICRONS')
start = datetime.datetime(2019,12,31)
end   = datetime.datetime(2020,12,31)

def fetch_price(ticker, start, end):
    try:
        print("start is :",start)
        print("End date: ",end)
        data = get_history(ticker, start, end)
    except:
        data= pd.DataFrame()
    return data

def get_prices(symbol):
    if not symbol:
        return
    if nse.is_valid_code(symbol):
        pass
    else:
        print("Invalid symbol passed")

    base_path = 'price_list/'
    if path.exists(base_path):
        print("base path exist")
        pass
    else:
        try:
            pat = os.path.join('.', base_path)
            os.makedirs(pat)
            print("base path creates successfully")
        except Exception as x:
            print(x)
            return -1

    fl_name = base_path + symbol + '.csv'
    if path.exists(fl_name):
        print(fl_name, 'file exist')
    else:
        print('file does not exist')
        print("getting %{}.csv",symbol)
        listing_date = date_of_listing(symbol)

        conv         = time.strptime(listing_date,"%d-%b-%Y")
        start_str    = time.strftime("%Y-%m-%d 00:00:00",conv)
        
        start        = datetime.datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')
        end          = datetime.datetime.now() #strptime(end_str, '%Y-%m-%d %H:%M:%S')
        
        prices = fetch_price(symbol, start, end)
        prices.to_csv(fl_name)

    return get_df(symbol) 
