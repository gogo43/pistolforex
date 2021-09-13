import streamlit as st
from datetime import date

import duka.app.app as import_tick_method
from duka.core.utils import TimeFrame
import datetime


import base64
import time
timestr =time.strftime("%Y%m%d-%H%M%S")
import pandas as pd
import glob
from glob import iglob
import os

st.title("PISTOLAIR FOREX TICK DOWNLOAD HISTORY FROM DUKASCOPY")
st.header('create by Pistolair')
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)


timeframes = ("TICK","M1", "M5", "M10", "M15", "M30", "H1", "H4","D1")
selected_timeframe = st.selectbox("Select timeframe for download", timeframes)

pairs = ("AUDCAD","AUDCHF", "AUDJPY", "AUDNZD", "AUDSGD", "CADCHF", "CADHKD", "CADJPY", "CHFJPY", "CHFSGD", "EURAUD", "EURCAD", "EURCHF", "EURGBP", "EURJPY","EURUSD","GBPAUD","GBPCAD","GBPCHF","GBPJPY","GBPNZD","GBPUSD","NZDUSD","NZDJPY","NZDCAD","NZDCHF","USDCAD","USDCHF","USDJPY")
selected_pairs = [st.selectbox("Select pairs for download", pairs)]

def csv_downloader(data):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = "DUKASCOPY_{}_.csv".format(timestr)
    st.markdown("#### Download File ###")
    href =f'<a href="data:file/csv;base64,{b64}" download = "{new_filename}">Click Here!!</a>'
    st.markdown(href,unsafe_allow_html=True)


#@st.cache
def load_data(tickers):
    if selected_timeframe == "TICK":
        data = import_tick_method(tickers, start_date, end_date, 1, TimeFrame.TICK , ".", True)
        return data 
    elif selected_timeframe == "D1":
        data = import_tick_method(tickers, start_date, end_date, 1, TimeFrame.D1 , ".", True)
        return data 
    elif selected_timeframe == "H4":
        data = import_tick_method(tickers, start_date, end_date, 1, TimeFrame.H4 , ".", True)
        return data 
    elif selected_timeframe == "H1":
        data = import_tick_method(tickers, start_date, end_date, 1, TimeFrame.H1 , ".", True)
        return data 
    elif selected_timeframe == "M30":
        data = import_tick_method(tickers, start_date, end_date, 1, TimeFrame.M30 , ".", True)
        return data 
    elif selected_timeframe == "M15":
        data = import_tick_method(tickers, start_date, end_date, 1, TimeFrame.M15 , ".", True)
        return data 
    elif selected_timeframe == "M10":
        data = import_tick_method(tickers, start_date, end_date, 1, TimeFrame.M10 , ".", True)
        return data 
    elif selected_timeframe == "M5":
        data = import_tick_method(tickers, start_date, end_date, 1, TimeFrame.M5 , ".", True)
        return data 
    elif selected_timeframe == "M1":
        data = import_tick_method(tickers, start_date, end_date, 1, TimeFrame.M1 , ".", True)
        return data 




submit = st.button('Submit')

st.write('Press submit to download data')

if submit:
    data_load_state = st.text("Load data... Sik Sabar ya....")
    data = load_data(selected_pairs)
    data_load_state.text("Loading data... done!")
    
       
    df = pd.read_csv(next(iglob('*.csv')))
    st.dataframe(df)
    csv_downloader(df)

    path = os.getcwd()
    csv_file =glob.glob(os.path.join(path, "*.csv"))

    for f in csv_file:
        df = pd.read_csv(f)
        
        File_name = f.split("/")[-1]
        st.write('location :', f)
        st.write('FIle Name :', File_name)

   
    

