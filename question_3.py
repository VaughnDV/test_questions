
"""
3. Write a set of classes ~20 mins
We have a sql table with 4 columns (id, url, date, rating). We need a set of classes that allows
us to build a query​ which can filter this table across any combination​ of these possibilities:
- id: >, <, =, IN, NOTIN
- url: =
- date: >, <, =
- rating: >, <, =
E.g. we may want all entries with: (2 < rating < 9) and​ (id in list) and​ (date > 1 Jan 2016).
The goal is to have a set of classes which enable easy testing wherever they are used (i.e. the
database does not have to be overly mocked every time). We want users of these classes to be
able to add filters without having to add to or rewrite tests.
"""

from datetime import datetime, timedelta, date
import pandas as pd
import numpy as np

class FindId:

    @staticmethod
    def greater_than(df, x):
        df = df.loc[df["id"] > x]
        return df
    
    @staticmethod
    def less_than(df, x):
        df = df.loc[df["id"] < x]
        return df

    @staticmethod
    def equal_to(df, x):
        df = df.loc[df["id"] == x]
        return df

    @staticmethod
    def is_in(df, x):
        df = df.loc[df["id"].isin(x) == True]
        return df
    
    @staticmethod
    def is_not_in(df, x):
        df = df.loc[df["id"].isin(x) == False]
        return df


class FindUrl:

    @staticmethod
    def equal_to(df, x):
        df = df.loc[df["url"] == x]
        return df


class FindDate:

    @staticmethod
    def greater_than(df, x):
        df = df.loc[df["date"] > x]
        return df

    @staticmethod
    def less_than(df, x):
        df = df.loc[df["date"] < x]
        return df

    @staticmethod
    def equal_to(df, x):
        df = df.loc[df["date"] == x]
        return df   


class FindRating:

    @staticmethod
    def greater_than(df, x):
        df = df.loc[df["rating"] > x]
        return df

    @staticmethod
    def less_than(df, x):
        df = df.loc[df["rating"] < x]
        return df

    @staticmethod
    def equal_to(df, x):
        df = df.loc[df["rating"] == x]
        return df
