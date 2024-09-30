"""
@author: andrescmendeza
Process validation to mag_workflow
"""

import pandas as pd # type: ignore
import re

def pre_process():
    data=pd.read_csv("~/ip_files/ventas.csv")

    if data.isnull().values.any():
        data=data.dropna(axis=0, how='any')
    
    data.to_csv("~/ip_files/ventas1.csv")