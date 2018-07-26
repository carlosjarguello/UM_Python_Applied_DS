#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:46:48 2017

Simple exercise, merging pandas dataframes

@author: carlosjarguello
"""

import pandas as pd

products = pd.DataFrame([{"Product ID": 4109, "Price":5.0, 'Product': 'Sushi Roll'},
                         {"Product ID": 1412, "Price":0.5, 'Product': 'Egg'},
                         {"Product ID": 8931, "Price":1.5, 'Product': 'Bagel'}],
                         )
products.set_index('Product ID', inplace = True)

invoices = pd.DataFrame([{"Costumer": 'Ali', "Product ID":4109, 'Quantity': 1},
                         {"Costumer": 'Eric', "Product ID":1412, 'Quantity': 12},
                         {"Costumer": 'Ande', "Product ID":8931, 'Quantity': 6},
                         {"Costumer": 'Sam', "Product ID":4109, 'Quantity': 2}])

print products
print invoices

new_df =  pd.merge(products, invoices, left_index = True, right_on = 'Product ID')
print new_df
def quantity_times_price(row):
    data = row[['Quantity','Price']]
    return pd.Series({'res': data.Quantity*data.Price})
    #return data.Quantity*data.Price
    
    
print new_df.apply(quantity_times_price, axis = 1)