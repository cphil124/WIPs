from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd
from pandas import DataFrame


class DataTransformer(object):
    
    def __init__(self, dataset):
        self.raw_data = None
        if dataset:
            self.raw_data = dataset
        self.working_set = None
        self.train_set = None
        self.valid_set = None
        pass

    def fit(self, X, y=None):
        return self  

    def get_recent_data_(self):
        if self.working_set is not None:
            data = self.working_set
        else:
            data = self.raw_data
        return data

    def X_per_Y(self, colX, colY):
        data = self.get_recent_data_()

        if colX in data and colY in data:
            new_header = colX + ' per ' + colY
            per_col = data[colX] / data[colY]
            return per_col, new_header


    def addColumn_(self, new_col, new_header):
        data = self.get_recent_data_()
        data[f'{new_header}'] = new_col
        self.working_set = data

    def addTransformedCol(self, trans_func, *cols):
        col, header = exec(f'{trans_func}({cols})')
        addColumn_(col, header)


x = DataTransformer()



        