from datetime import datetime
import pandas as pd
import pytz
from zipline import run_algorithm, get_calendar
from zipline.api import symbol, order, record, sid

def initialize(context):
    context.i = 0
    assets = context.asset_finder.sids #something like this
    assert len(assets) >= 1
    print(context.sid(assets[0]))
    context.asset = context.sid(assets[0])
    context.security = sid(0)
#    pass

def handle_data(context, data):
    order(context.security, 10)
    record(日本水産=data[context.security].price)

start = pd.Timestamp(datetime(2018, 1, 1, tzinfo=pytz.UTC))
end = pd.Timestamp(datetime(2018, 7, 25, tzinfo=pytz.UTC))

perf = run_algorithm(start=start,
                        end=end,
                        initialize=initialize,
                        capital_base=100000,
                        handle_data=handle_data,
                        data_frequency='daily',
                        bundle='csvdir',
                        trading_calendar=get_calendar('JPX'))

df=pd.DataFrame(perf)
print(df['returns'])

# run_algorithm(start=start,
#               end=end,
#               initialize=initialize,
#               capital_base=100000,
#               handle_data=handle_data,
#               before_trading_start=before_trading_start,
#               data_frequency='daily')
