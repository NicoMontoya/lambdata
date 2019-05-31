#!/usr/bin/env python
"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd 
import numpy as np 
from . import explore_nulls 

TEST = pd.DataFrame(np.ones(10)) 

def check_nulls(df):
    """
    Prints out columns and numbers of nan's it has
    """
    print(df.isna().sum())

def split_date(dates):
    """
    Function to split dates ("MM/DD/YYYY", etc.) into multiple columns
    Returns dataframe called 'dates' containing three new columns
    """
    split_dates = pd.DataFrame()
    dates = pd.to_datetime(dates, format='%Y-%m-%d')
    split_dates['year'] = dates.dt.year
    split_dates['month'] = dates.dt.month 
    split_dates['day'] = dates.dt.day

    return split_dates 


