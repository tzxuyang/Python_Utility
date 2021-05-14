# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:41:07 2021

@author: YXU71
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askopenfilenames
import re


Tk().withdraw()
filename = askopenfilename(title='Select base file (the format to be used)')
print('Loading ...', filename)
base_db = pd.read_csv(filename, index_col= False)

colmn_select = base_db.columns.values.tolist()


filenames = askopenfilenames(title='Select files to append')
for this_file in filenames:
    print('Loading ...', this_file)
    new_db = pd.read_csv(this_file, index_col= False)
    colmn_new = new_db.columns.values.tolist()
    colmn_comb = list(set(colmn_new) & set(colmn_select))
    new_db = new_db[colmn_comb]
    base_db = base_db.append(new_db)

base_db.reset_index(drop=True, inplace=True)

filename_tmp = filename.replace('.','/')
filename_list = filename_tmp.split('/')
filename_save = filename_list[len(filename_list)-2] + '_combined.csv'


column_name = ' '
while len(column_name)>0:
    column_name = input ('Do you want to add an extra column? Input the name if yes, press enter if not: ')
    if len(column_name)>0:
        column_entry = input ('Input default entry of the column: ')
        base_db[column_name] = column_entry

base_db.to_csv(filename_save, index = False)