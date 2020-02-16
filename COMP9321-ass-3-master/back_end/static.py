"""
    Static variables (consts) to be used in the API (both internally & externally)
"""
STATE_INFO = {
    'ACT' : {'region_id' : '01', 'full_name' : 'Australian Capital Territory', 'is_state' : True},
    'NSW' : {'region_id' : '02', 'full_name' : 'New South Wales', 'is_state' : True},
    'VIC' : {'region_id' : '03', 'full_name' : 'Victoria', 'is_state' : True},
    'QLD' : {'region_id' : '04', 'full_name' : 'Queensland', 'is_state' : True},
    'SA' :  {'region_id' : '05', 'full_name' : 'South Australia', 'is_state' : True},
    'WA' :  {'region_id' : '06', 'full_name' : 'Western Australia', 'is_state' : True},
    'TAS' : {'region_id' : '07', 'full_name' : 'Tasmania', 'is_state' : True},
    'NT' :  {'region_id' : '08', 'full_name' : 'Northern Territory', 'is_state' : True},
}
AUS_INFO = {'AUS' : {'region_id' : '00', 'long_name' : 'Australia', 'is_state' : False}}
REGIONS_INFO = {**AUS_INFO, **STATE_INFO}

STATE_NAMES = list(STATE_INFO.keys())
REGION_NAMES = list(REGIONS_INFO.keys())

AGE_BANDS = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29',
    '30-34', '35-39', '40-44', '45-49', '50-54','55-59', '60-64',
    '65-69', '70-74', '75-79', '80-84', '85 and over']


PREDICTION_RANGE = (2019, 3019)

MDB_HOST = "mongodb://admin:9321admin@ds131763.mlab.com:31763/9321-ass-3"
MDB_COL_TOKENS = "tokens"

ADMIN_USER = 'admin'
ADMIN_PASS = 'admin123'
