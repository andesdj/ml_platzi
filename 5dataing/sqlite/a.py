from sqlalchemy import Column, Integer, Text, MetaData, Table
import pandas as pd


df= pd.read_csv('c.csv')
print(df.head())