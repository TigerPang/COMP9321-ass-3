"""
    Extracts data from spreadsheets into DataFrames to be used
      for training the ML model.
"""

import pandas
import os
import re

DATA_LOC = 'raw_data'
DATA_BY_STATE_LOC = os.path.join(DATA_LOC, 'States - 3105065001DS0001_2014.xls')
DATA_BY_GENDER_AGE_LOC = os.path.join(DATA_LOC, 'Age & Gender - 3105065001DS0002_2014.xls')

REGION_SHEETS = {
    'AUS' : 1,
    'NSW' : 4,
    'VIC' : 6,
    'QLD' : 8,
    'SA' : 10,
    'WA' : 12,
    'TAS' : 15,
    'NT' : 16,
    'ACT' : 17
}


"""
    Returns data for all of australia and every state
      and territory
"""
def get_region_data():
    df = _get_gender_state_data()
    df.drop(columns=[x for x in df.columns if not x.startswith('Persons')], inplace=True)
    df.rename(columns=lambda x: re.sub('[^A-Z].*','',x.replace('Persons - ','').upper()),inplace=True)
    df.rename(columns=lambda x: 'AUS' if x == 'AUSTRALIA' else x, inplace=True)
    df.fillna(0,inplace=True)
    return df

"""
    Returns data for each gender for a specific region.
"""
def get_gender_data(region='AUS'):
    #TODO check region
    df = _get_gender_state_data()
    df.drop(columns=[x for x in df.columns if x.startswith('Persons')], inplace=True)
    df.rename(columns=lambda x: re.sub('[\(\.].*$','',x.upper()),inplace=True)
    df.rename(columns=lambda x: re.sub('AUSTRALIA','AUS',x), inplace=True)
    df.drop(columns=[x for x in df.columns if not x.endswith(region)],inplace=True)
    df.rename(columns=lambda x: re.sub(' -.*$','',x), inplace=True)
    return df


"""
    Returns data for each age_band for a specific region.
"""
def get_age_data(region='AUS'):
    #TODO check region
    df = _get_gender_age_data(region)
    df.drop(columns=[x for x in df.columns if not x.startswith('Persons')], inplace=True)
    df.rename(columns=lambda x: re.sub('^.* - ','',x), inplace=True)
    df.drop(columns=['Total'],inplace=True,errors='ignore')
    return df


"""
    Returns dataframe for population counts per state & gender.

    Index is years (1901 - 2011).

    Column names are of the format "GENDER - STATE_OR_TERRITORY"
        Where "GENDER" is in: ["Males", "Females", "Persons"]
        And "STATE_OR_TERRITORY" is a state, territory or all of Australia
          including external territories.
"""
def _get_gender_state_data():

    df = pandas.read_excel(DATA_BY_STATE_LOC, sheet_name=2,
         header=4, index_col=0, skipfooter=12)

    df.dropna(how='all',inplace=True)

    # flip so we can index by year
    df = df.transpose()

    # rename columns so gender is placed before state
    df.columns = _get_gendered_columns(df)

    return df


"""
    Returns dataframe for population counts for each age group and gender
    for a specified state (or all of Australia).

    Since data is not available consecutively until 1971, by default this
    data is excluded. It can be included by setting:
        all_years=True


    Index is years (1901 - 2011).

    Column names are of the format "GENDER - AGE_BAND"
        Where "GENDER" is in: ["Males", "Females", "Persons"]
        And "AGE_BAND" is an ABS standard 5 year age band.
"""

def _get_gender_age_data(state='AUSTRALIA', all_years=False):
    sheet_id = REGION_SHEETS.get(state.upper())

    if sheet_id == None:
        raise ValueError('"%s" is not a valid state.' % state)

    df = pandas.read_excel(DATA_BY_GENDER_AGE_LOC, sheet_name=sheet_id,
         header=4,index_col=0, skipfooter=12)

    df.dropna(how='all', inplace=True)

    # flip so we can index by year
    df = df.transpose()

    # drop columns unrequired columns
    # (unrequired == columns that aren't age groups or "Total")
    df.drop(columns=[c for c in df.columns if not re.match('^(\d+(-\d+| and over)|Total)$',c)],
        inplace=True)

    df.columns = _get_gendered_columns(df)

    # state & territory sheets by default only have counts every year from 1971
    # so, unless all_years == True, we drop rows before 1971
    if all_years != True:
        df = df.loc[1971:]

    return df

"""
    Returns a list of column names from the passed dataframe
        with gender appended to the front.
"""
def _get_gendered_columns(df):
    col_genders = ['Males', 'Females', 'Persons']

    # first 1/n columns will have the first gender assigned, second
    # 1/n columns will have the second gender, ... etc
    # (for n = number of genders)
    col_partition = len(df.columns)/len(col_genders)
    return [col_genders[int(i/col_partition)] + ' - '+ c for i,c in enumerate(df.columns)]

