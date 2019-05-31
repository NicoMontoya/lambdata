import pandas as pd  
import numpy as np

class ExploreNulls:

    def __init__(self, df=pd.DataFrame(np.ones(10), columns=['ones'])):
        """Explore the nulls in a dataframe
        
        Keyword arguments:
        df -- a pandas DataFrame
        """
        self.df = df

    def show_nulls(self):
        """Show number of nulls in each column

        Keyword arguments:
        """

        return self.df.isna().sum()