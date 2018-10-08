import pandas as pd

class CLeanCSV:
    """A simple Python 3 tool to Clean csv files without hassle"""
    def __init__(self):

    #def getCSV(self,filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, skiprows=None, nrows=None):

    def getCSV(file_name, header = None, dropna = "", cols_index, col_names, ):
        review = pd.read_csv(file_name, header = header)
