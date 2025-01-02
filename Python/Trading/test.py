from datetime import date
from nsepy import get_history
from nsepy.derivatives import get_expiry_date

sbin = get_history(symbol='SBIN',
                   start=date(2023,1,1),
                   end=date(2023,1,5))
# print (sbin)
# print (get_expiry_date(2022,1))
dates = get_expiry_date(2023,1)
# print (list(dates)[5])
#print (list(dates)[5].strftime("%d/%m/%Y"))

stock_fut = get_history(symbol="SBIN",
                            start=date(2023,1,1),
                            end=date(2023,1,10),
                            futures=True,
                            expiry_date=list(dates)[5])

print (stock_fut)

# stock_opt = get_history(symbol="SBIN",
#                         start=date(2015,1,1),
#                         end=date(2015,1,10),
#                         option_type="CE",
#                         strike_price=300,
#                         expiry_date=get_expiry_date(2022,1))

# nifty_fut = get_history(symbol="NIFTY",
#                         start=date(2015,1,1),
#                         end=date(2015,1,10),
#                         index=True,
#                         futures=True,
#                         expiry_date=get_expiry_date(2022,1))

# nifty_opt = get_history(symbol="NIFTY",
#                         start=date(2015,1,1),
#                         end=date(2015,1,10),
#                         index=True,
#                         option_type='CE',
#                         strike_price=8200,
#                         expiry_date=get_expiry_date(2022,1))