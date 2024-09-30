"""
@author: andrescmendeza
Process validation to mag_workflow
"""

import pandas as pd # type: ignore
from datetime import date

now = date.today()
dt_string = now.strftime("%d-%m-%Y")

def process_data():
    data=pd.read_csv("~/ip_files/ventas.csv")
    data['Despacho']= 'S'
    data.to_csv("~/op_files/final.csv",index=False)